from __future__ import annotations

import os
import shutil
import struct
import uuid
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from docx import Document
from docx.enum.section import WD_SECTION_START
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(r"C:\Francois\Writting\HomoNoxisGithub")
TARGET = ROOT / "HomoNoxius-reference.docx"
WORK = ROOT / "tmp" / "docx"
BASE = WORK / "HomoNoxius-reference.base.docx"
BUILT = WORK / "HomoNoxius-reference.built.docx"
FONT_DIR = Path(r"C:\Francois\Writting\EB_Garamond\static")

FONT = "EB Garamond"
INK = RGBColor(0x1E, 0x1B, 0x18)
GOLD = "8A6A2A"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"


def remove_children(parent, tag):
    for child in list(parent):
        if child.tag == tag:
            parent.remove(child)


def set_bool(parent, tag, value=True):
    remove_children(parent, qn(tag))
    if value:
        parent.append(OxmlElement(tag))


def set_attr_child(parent, tag, **attrs):
    remove_children(parent, qn(tag))
    child = OxmlElement(tag)
    for key, value in attrs.items():
        child.set(qn(key), str(value))
    parent.append(child)
    return child


def set_style_font(style, size, *, bold=False, italic=False, small_caps=False,
                   tracking=0, color=INK):
    style.font.name = FONT
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.italic = italic
    style.font.small_caps = small_caps
    style.font.color.rgb = color
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), FONT)
    set_attr_child(rpr, "w:lang", **{"w:val": "en-GB", "w:eastAsia": "en-GB", "w:bidi": "en-GB"})
    if tracking:
        set_attr_child(rpr, "w:spacing", **{"w:val": tracking})
    else:
        remove_children(rpr, qn("w:spacing"))


def set_style_paragraph(style, *, alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
                        before=0, after=0, line=1.065, first=0,
                        left=0, right=0, keep_next=False, keep_together=False,
                        page_break=False, widow=True):
    pf = style.paragraph_format
    pf.alignment = alignment
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.line_spacing = line
    pf.first_line_indent = Pt(first)
    pf.left_indent = Inches(left)
    pf.right_indent = Inches(right)
    pf.keep_with_next = keep_next
    pf.keep_together = keep_together
    pf.page_break_before = page_break
    pf.widow_control = widow


def set_border(style, *, side, color=GOLD, size=3, space=8, value="single"):
    ppr = style.element.get_or_add_pPr()
    pbdr = ppr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr")
        ppr.append(pbdr)
    remove_children(pbdr, qn(f"w:{side}"))
    border = OxmlElement(f"w:{side}")
    border.set(qn("w:val"), value)
    border.set(qn("w:sz"), str(size))
    border.set(qn("w:space"), str(space))
    border.set(qn("w:color"), color)
    pbdr.append(border)


def clear_borders(style):
    ppr = style.element.get_or_add_pPr()
    remove_children(ppr, qn("w:pBdr"))


def get_or_add_style(doc, name, base="Normal"):
    try:
        style = doc.styles[name]
    except KeyError:
        style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    style.base_style = doc.styles[base]
    style.hidden = False
    style.unhide_when_used = False
    style.quick_style = True
    return style


def set_next(style, next_style):
    style.next_paragraph_style = next_style


def clear_paragraph(paragraph):
    for child in list(paragraph._p):
        if child.tag not in (qn("w:pPr"),):
            paragraph._p.remove(child)


def format_direct_run(run, size=9, *, small_caps=True, italic=False):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.small_caps = small_caps
    run.font.italic = italic
    run.font.color.rgb = INK
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), FONT)


def add_field(paragraph, instruction, placeholder, *, size=9, small_caps=False):
    run = paragraph.add_run()
    format_direct_run(run, size=size, small_caps=small_caps)
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    begin.set(qn("w:dirty"), "true")
    instr = OxmlElement("w:instrText")
    instr.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    instr.text = f" {instruction} "
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t")
    text.text = placeholder
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.extend([begin, instr, separate, text, end])
    return run


def configure_header_paragraph(paragraph, alignment):
    clear_paragraph(paragraph)
    paragraph.alignment = alignment
    paragraph.paragraph_format.space_before = Pt(0)
    paragraph.paragraph_format.space_after = Pt(0)
    paragraph.paragraph_format.line_spacing = 1.0


def configure_document(doc):
    section = doc.sections[0]
    section.start_type = WD_SECTION_START.NEW_PAGE
    section.page_width = Inches(6)
    section.page_height = Inches(9)
    section.top_margin = Inches(0.72)
    section.bottom_margin = Inches(0.76)
    section.left_margin = Inches(0.70)
    section.right_margin = Inches(0.70)
    section.header_distance = Inches(0.30)
    section.footer_distance = Inches(0.28)
    section.gutter = Inches(0)
    section.different_first_page_header_footer = True
    doc.settings.odd_and_even_pages_header_footer = True

    settings = doc.settings.element
    set_bool(settings, "w:mirrorMargins", True)
    set_bool(settings, "w:embedTrueTypeFonts", True)
    set_bool(settings, "w:doNotHyphenateCaps", True)
    set_attr_child(settings, "w:autoHyphenation", **{"w:val": "true"})
    set_attr_child(settings, "w:consecutiveHyphenLimit", **{"w:val": "2"})
    set_attr_child(settings, "w:hyphenationZone", **{"w:val": "144"})

    normal = doc.styles["Normal"]
    clear_borders(normal)
    set_style_font(normal, 11)
    set_style_paragraph(normal, first=12.65, line=1.065)

    body = doc.styles["Body Text"]
    body.base_style = normal
    clear_borders(body)
    set_style_font(body, 11)
    set_style_paragraph(body, first=12.65, line=1.065)

    first = doc.styles["First Paragraph"]
    first.base_style = normal
    clear_borders(first)
    set_style_font(first, 11)
    set_style_paragraph(first, first=0, line=1.065)

    compact = doc.styles["Compact"]
    compact.base_style = normal
    clear_borders(compact)
    set_style_font(compact, 10)
    set_style_paragraph(compact, first=0, line=1.02)

    title = doc.styles["Title"]
    title.base_style = normal
    clear_borders(title)
    set_style_font(title, 24.8, small_caps=True)
    set_style_paragraph(title, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=90, after=25, line=1.0, left=0.95, right=0.95,
                        keep_next=True, widow=False)
    set_border(title, side="bottom", size=3, space=16)

    subtitle = doc.styles["Subtitle"]
    subtitle.base_style = normal
    clear_borders(subtitle)
    set_style_font(subtitle, 11, italic=True)
    set_style_paragraph(subtitle, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=0, after=8, line=1.0, first=0)

    for name, size, italic in (("Author", 10, False), ("Date", 9, False)):
        style = doc.styles[name]
        style.base_style = normal
        clear_borders(style)
        set_style_font(style, size, italic=italic)
        set_style_paragraph(style, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                            before=4, after=4, line=1.0, first=0)

    abstract = doc.styles["Abstract"]
    abstract.base_style = normal
    clear_borders(abstract)
    set_style_font(abstract, 10.5, italic=True)
    set_style_paragraph(abstract, alignment=WD_ALIGN_PARAGRAPH.LEFT,
                        before=18, after=10, line=1.04, first=0,
                        left=0.55, right=0.55)

    abstract_title = doc.styles["Abstract Title"]
    abstract_title.base_style = normal
    clear_borders(abstract_title)
    set_style_font(abstract_title, 12, small_caps=True)
    set_style_paragraph(abstract_title, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=18, after=8, line=1.0, first=0, keep_next=True)

    heading1 = doc.styles["Heading 1"]
    heading1.base_style = normal
    clear_borders(heading1)
    set_style_font(heading1, 17.2, small_caps=True)
    set_style_paragraph(heading1, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=76, after=12, line=1.0, first=0,
                        keep_next=True, page_break=True, widow=False)

    heading2 = doc.styles["Heading 2"]
    heading2.base_style = normal
    clear_borders(heading2)
    set_style_font(heading2, 14.35, small_caps=True)
    set_style_paragraph(heading2, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=28, after=10, line=1.0, first=0, keep_next=True)

    heading3 = doc.styles["Heading 3"]
    heading3.base_style = normal
    clear_borders(heading3)
    set_style_font(heading3, 11, small_caps=True, tracking=8)
    set_style_paragraph(heading3, alignment=WD_ALIGN_PARAGRAPH.LEFT,
                        before=16, after=6, line=1.0, first=0, keep_next=True)

    for idx in range(4, 10):
        style = doc.styles[f"Heading {idx}"]
        style.base_style = normal
        clear_borders(style)
        set_style_font(style, max(9, 12 - (idx - 4) * 0.5), small_caps=idx < 7)
        set_style_paragraph(style, alignment=WD_ALIGN_PARAGRAPH.LEFT,
                            before=12, after=4, line=1.0, first=0, keep_next=True)

    block = doc.styles["Block Text"]
    block.base_style = normal
    clear_borders(block)
    set_style_font(block, 10.5)
    set_style_paragraph(block, alignment=WD_ALIGN_PARAGRAPH.LEFT,
                        before=6, after=6, line=1.04, first=0,
                        left=0.35, right=0.35)

    for name in ("Footnote Text", "Footnote Block Text"):
        style = doc.styles[name]
        style.base_style = normal
        clear_borders(style)
        set_style_font(style, 9)
        set_style_paragraph(style, alignment=WD_ALIGN_PARAGRAPH.LEFT,
                            before=0, after=0, line=1.0, first=0)

    for name in ("Table Caption", "Image Caption", "Caption"):
        style = doc.styles[name]
        style.base_style = normal
        clear_borders(style)
        set_style_font(style, 9, italic=True)
        set_style_paragraph(style, alignment=WD_ALIGN_PARAGRAPH.CENTER,
                            before=6, after=8, line=1.0, first=0, keep_next=True)

    custom = {}
    custom["HN Chapter Number"] = get_or_add_style(doc, "HN Chapter Number")
    set_style_font(custom["HN Chapter Number"], 10, small_caps=True, tracking=24)
    set_style_paragraph(custom["HN Chapter Number"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=76, after=26, line=1.0, first=0,
                        keep_next=True, page_break=True, widow=False)

    custom["HN Chapter Title"] = get_or_add_style(doc, "HN Chapter Title")
    set_style_font(custom["HN Chapter Title"], 17.2, small_caps=True)
    set_style_paragraph(custom["HN Chapter Title"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=0, after=2, line=1.0, first=0, keep_next=True, widow=False)

    custom["HN Chapter Rule"] = get_or_add_style(doc, "HN Chapter Rule")
    set_style_font(custom["HN Chapter Rule"], 1)
    set_style_paragraph(custom["HN Chapter Rule"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=0, after=43, line=1.0, first=0,
                        left=1.52, right=1.52, keep_next=True, widow=False)
    set_border(custom["HN Chapter Rule"], side="bottom", size=3, space=0)

    custom["HN Location"] = get_or_add_style(doc, "HN Location")
    set_style_font(custom["HN Location"], 9, italic=True)
    set_style_paragraph(custom["HN Location"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=0, after=12, line=1.0, first=0)

    custom["HN Book Label"] = get_or_add_style(doc, "HN Book Label")
    set_style_font(custom["HN Book Label"], 14.35, small_caps=True, tracking=32)
    set_style_paragraph(custom["HN Book Label"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=151, after=22, line=1.0, first=0,
                        keep_next=True, page_break=True, widow=False)

    custom["HN Book Title"] = get_or_add_style(doc, "HN Book Title")
    set_style_font(custom["HN Book Title"], 24.8, italic=True)
    set_style_paragraph(custom["HN Book Title"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=0, after=0, line=1.0, first=0,
                        left=0.95, right=0.95, keep_next=True, widow=False)
    set_border(custom["HN Book Title"], side="bottom", size=3, space=18)

    custom["HN Front Matter Heading"] = get_or_add_style(doc, "HN Front Matter Heading")
    set_style_font(custom["HN Front Matter Heading"], 14.35, small_caps=True)
    set_style_paragraph(custom["HN Front Matter Heading"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=97, after=12, line=1.0, first=0,
                        keep_next=True, page_break=True, widow=False)

    custom["HN Dedication"] = get_or_add_style(doc, "HN Dedication")
    set_style_font(custom["HN Dedication"], 10.9, italic=True)
    set_style_paragraph(custom["HN Dedication"], alignment=WD_ALIGN_PARAGRAPH.LEFT,
                        before=90, after=0, line=1.04, first=0,
                        left=0.75, right=0.75)

    custom["HN Scripture Title"] = get_or_add_style(doc, "HN Scripture Title")
    set_style_font(custom["HN Scripture Title"], 12, small_caps=True)
    set_style_paragraph(custom["HN Scripture Title"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=14, after=4, line=1.0, first=0, keep_next=True)

    custom["HN Scripture Subtitle"] = get_or_add_style(doc, "HN Scripture Subtitle")
    set_style_font(custom["HN Scripture Subtitle"], 10.9, italic=True)
    set_style_paragraph(custom["HN Scripture Subtitle"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=0, after=10, line=1.0, first=0, keep_next=True)

    custom["HN Scripture"] = get_or_add_style(doc, "HN Scripture")
    set_style_font(custom["HN Scripture"], 10, italic=True)
    set_style_paragraph(custom["HN Scripture"], alignment=WD_ALIGN_PARAGRAPH.LEFT,
                        before=0, after=0, line=1.04, first=0,
                        left=0.35, right=0.69)

    for level, indent in ((1, 0.18), (2, 0.36), (3, 0.54)):
        name = f"HN Room {level}"
        style = get_or_add_style(doc, name)
        custom[name] = style
        set_style_font(style, 10)
        set_style_paragraph(style, alignment=WD_ALIGN_PARAGRAPH.LEFT,
                            before=0, after=3.5, line=1.04, first=0,
                            left=indent, right=0)
        set_border(style, side="left", size=10, space=9)

    custom["HN Room Direction"] = get_or_add_style(doc, "HN Room Direction", "HN Room 1")
    set_style_font(custom["HN Room Direction"], 10, italic=True)
    set_style_paragraph(custom["HN Room Direction"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=2, after=3.5, line=1.0, first=0, left=0.18)
    set_border(custom["HN Room Direction"], side="left", size=10, space=9)

    custom["HN Scene Break"] = get_or_add_style(doc, "HN Scene Break")
    set_style_font(custom["HN Scene Break"], 1)
    set_style_paragraph(custom["HN Scene Break"], alignment=WD_ALIGN_PARAGRAPH.CENTER,
                        before=10, after=12, line=1.0, first=0,
                        left=1.61, right=1.61, keep_next=True, widow=False)
    set_border(custom["HN Scene Break"], side="bottom", size=2, space=0)

    custom["HN Declaration"] = get_or_add_style(doc, "HN Declaration")
    set_style_font(custom["HN Declaration"], 11)
    set_style_paragraph(custom["HN Declaration"], alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
                        before=0, after=5.5, line=1.0, first=0)

    custom["HN Founder Verse"] = get_or_add_style(doc, "HN Founder Verse")
    set_style_font(custom["HN Founder Verse"], 11)
    set_style_paragraph(custom["HN Founder Verse"], alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
                        before=0, after=0, line=1.08, first=-19.8,
                        left=0.275, right=0)

    custom["HN Source Note"] = get_or_add_style(doc, "HN Source Note")
    set_style_font(custom["HN Source Note"], 9, italic=True)
    set_style_paragraph(custom["HN Source Note"], alignment=WD_ALIGN_PARAGRAPH.LEFT,
                        before=3, after=6, line=1.0, first=0)

    set_next(title, subtitle)
    set_next(subtitle, doc.styles["Author"])
    set_next(heading1, first)
    set_next(custom["HN Chapter Number"], custom["HN Chapter Title"])
    set_next(custom["HN Chapter Title"], custom["HN Chapter Rule"])
    set_next(custom["HN Chapter Rule"], custom["HN Location"])
    set_next(custom["HN Location"], first)
    set_next(custom["HN Scripture Title"], custom["HN Scripture Subtitle"])
    set_next(custom["HN Scripture Subtitle"], custom["HN Scripture"])

    primary_header = section.header.paragraphs[0]
    configure_header_paragraph(primary_header, WD_ALIGN_PARAGRAPH.RIGHT)
    add_field(primary_header, 'STYLEREF "Heading 1"', "Chapter", size=9, small_caps=True)

    even_header = section.even_page_header.paragraphs[0]
    configure_header_paragraph(even_header, WD_ALIGN_PARAGRAPH.LEFT)
    run = even_header.add_run("Homo Noxius")
    format_direct_run(run, size=9, small_caps=True)

    first_header = section.first_page_header.paragraphs[0]
    configure_header_paragraph(first_header, WD_ALIGN_PARAGRAPH.CENTER)

    primary_footer = section.footer.paragraphs[0]
    configure_header_paragraph(primary_footer, WD_ALIGN_PARAGRAPH.RIGHT)
    add_field(primary_footer, "PAGE", "1", size=9, small_caps=False)

    even_footer = section.even_page_footer.paragraphs[0]
    configure_header_paragraph(even_footer, WD_ALIGN_PARAGRAPH.LEFT)
    add_field(even_footer, "PAGE", "2", size=9, small_caps=False)

    first_footer = section.first_page_footer.paragraphs[0]
    configure_header_paragraph(first_footer, WD_ALIGN_PARAGRAPH.CENTER)

    marker = "Homo Noxius custom styles"
    if not any(p.text == marker for p in doc.paragraphs):
        doc.add_page_break()
        doc.add_paragraph(marker, style="Heading 2")
        doc.add_paragraph("Chapter 1", style="HN Chapter Number")
        doc.add_paragraph("Ascension", style="HN Chapter Title")
        doc.add_paragraph("", style="HN Chapter Rule")
        doc.add_paragraph("Blackwood Estate — the Swiss Alps", style="HN Location")
        doc.add_paragraph("Narrative body. The first paragraph opens without an indent and returns to the ordinary measure.", style="First Paragraph")
        doc.add_paragraph("The following paragraph carries the regular first-line indent, justified measure, and restrained rhythm of the manuscript.", style="Body Text")
        doc.add_paragraph("", style="HN Scene Break")
        doc.add_paragraph("— The recorder continues. This is the outer room.", style="HN Room 1")
        doc.add_paragraph("— A second documentary enclosure begins inside it.", style="HN Room 2")
        doc.add_paragraph("[A sound crosses the innermost room.]", style="HN Room Direction")
        doc.add_paragraph("— The third enclosure remains legible without becoming a heading.", style="HN Room 3")
        doc.add_paragraph("Outsider Copy", style="HN Scripture Title")
        doc.add_paragraph("A recovered manuscript of the Sixth Cycle", style="HN Scripture Subtitle")
        doc.add_paragraph("And God said, Fear not the darkness which I have given thee; for the darkness shall be thy veil.", style="HN Scripture")
        doc.add_paragraph("The declaration remains upright, unindented, and separated by measured paragraph space.", style="HN Declaration")
        doc.add_paragraph("A founder’s verse begins at the margin; any natural continuation hangs beneath the words that opened it.", style="HN Founder Verse")
        doc.add_paragraph("Editorial or documentary source note.", style="HN Source Note")

    doc.core_properties.title = "Homo Noxius — Pandoc reference document"
    doc.core_properties.subject = "Word style system matched to the 6 × 9 inch Homo Noxius edition"
    doc.core_properties.comments = "Reference styles only; Pandoc ignores the sample body when generating a manuscript."


def obfuscate_font(font_bytes, guid):
    data = bytearray(font_bytes)
    key = guid.bytes_le
    for idx in range(min(32, len(data))):
        data[idx] ^= key[15 - (idx % 16)]
    return bytes(data)


def font_fs_type(font_path):
    data = font_path.read_bytes()
    num_tables = struct.unpack(">H", data[4:6])[0]
    for idx in range(num_tables):
        pos = 12 + idx * 16
        tag = data[pos:pos + 4]
        if tag == b"OS/2":
            offset = struct.unpack(">I", data[pos + 8:pos + 12])[0]
            return struct.unpack(">H", data[offset + 8:offset + 10])[0]
    raise ValueError(f"OS/2 table not found in {font_path}")


def embed_fonts(source, destination):
    font_specs = [
        ("regular", FONT_DIR / "EBGaramond-Regular.ttf", "embedRegular"),
        ("bold", FONT_DIR / "EBGaramond-Bold.ttf", "embedBold"),
        ("italic", FONT_DIR / "EBGaramond-Italic.ttf", "embedItalic"),
        ("boldItalic", FONT_DIR / "EBGaramond-BoldItalic.ttf", "embedBoldItalic"),
    ]
    for _, path, _ in font_specs:
        if font_fs_type(path) & 0x0002:
            raise PermissionError(f"Embedding is restricted by {path.name}")

    with zipfile.ZipFile(source, "r") as zin:
        parts = {name: zin.read(name) for name in zin.namelist()}

    ET.register_namespace("w", W_NS)
    ET.register_namespace("r", R_NS)
    ET.register_namespace("", PKG_REL_NS)

    font_table = ET.fromstring(parts["word/fontTable.xml"])
    for node in list(font_table):
        if node.tag == f"{{{W_NS}}}font" and node.get(f"{{{W_NS}}}name") == FONT:
            font_table.remove(node)
    font_node = ET.SubElement(font_table, f"{{{W_NS}}}font", {f"{{{W_NS}}}name": FONT})
    ET.SubElement(font_node, f"{{{W_NS}}}family", {f"{{{W_NS}}}val": "roman"})
    ET.SubElement(font_node, f"{{{W_NS}}}pitch", {f"{{{W_NS}}}val": "variable"})
    ET.SubElement(font_node, f"{{{W_NS}}}charset", {f"{{{W_NS}}}val": "00"})

    rel_path = "word/_rels/fontTable.xml.rels"
    if rel_path in parts:
        rels = ET.fromstring(parts[rel_path])
    else:
        rels = ET.Element(f"{{{PKG_REL_NS}}}Relationships")
    used_ids = {node.get("Id") for node in rels}

    for ordinal, (label, path, element_name) in enumerate(font_specs, 1):
        rid = f"rIdHNFont{ordinal}"
        if rid in used_ids:
            raise ValueError(f"Unexpected duplicate font relationship: {rid}")
        guid = uuid.uuid4()
        target_name = f"EBGaramond-{label}.odttf"
        parts[f"word/fonts/{target_name}"] = obfuscate_font(path.read_bytes(), guid)
        ET.SubElement(
            rels,
            f"{{{PKG_REL_NS}}}Relationship",
            {
                "Id": rid,
                "Type": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/font",
                "Target": f"fonts/{target_name}",
            },
        )
        ET.SubElement(
            font_node,
            f"{{{W_NS}}}{element_name}",
            {
                f"{{{R_NS}}}id": rid,
                f"{{{W_NS}}}fontKey": "{" + str(guid).upper() + "}",
                f"{{{W_NS}}}subsetted": "0",
            },
        )

    content_types = ET.fromstring(parts["[Content_Types].xml"])
    if not any(node.tag == f"{{{CT_NS}}}Default" and node.get("Extension") == "odttf" for node in content_types):
        ET.SubElement(
            content_types,
            f"{{{CT_NS}}}Default",
            {
                "Extension": "odttf",
                "ContentType": "application/vnd.openxmlformats-officedocument.obfuscatedFont",
            },
        )

    parts["word/fontTable.xml"] = ET.tostring(font_table, encoding="utf-8", xml_declaration=True)
    parts[rel_path] = ET.tostring(rels, encoding="utf-8", xml_declaration=True)
    parts["[Content_Types].xml"] = ET.tostring(content_types, encoding="utf-8", xml_declaration=True)

    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in parts.items():
            zout.writestr(name, data)


def validate(path):
    with zipfile.ZipFile(path, "r") as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f"Corrupt ZIP member: {bad}")
        names = set(archive.namelist())
        required = {
            "word/document.xml",
            "word/styles.xml",
            "word/settings.xml",
            "word/fontTable.xml",
            "word/_rels/fontTable.xml.rels",
            "word/fonts/EBGaramond-regular.odttf",
            "word/fonts/EBGaramond-bold.odttf",
            "word/fonts/EBGaramond-italic.odttf",
            "word/fonts/EBGaramond-boldItalic.odttf",
        }
        missing = required - names
        if missing:
            raise ValueError(f"Missing DOCX parts: {sorted(missing)}")
    doc = Document(path)
    section = doc.sections[0]
    assert round(section.page_width.inches, 2) == 6.00
    assert round(section.page_height.inches, 2) == 9.00
    for style_name in (
        "HN Chapter Number", "HN Chapter Title", "HN Chapter Rule",
        "HN Scripture", "HN Room 1", "HN Room 2", "HN Room 3",
        "HN Scene Break", "HN Declaration", "HN Founder Verse",
    ):
        doc.styles[style_name]


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    if not TARGET.exists():
        raise FileNotFoundError(TARGET)
    doc = Document(TARGET)
    configure_document(doc)
    doc.save(BASE)
    embed_fonts(BASE, BUILT)
    validate(BUILT)
    os.replace(BUILT, TARGET)
    BASE.unlink(missing_ok=True)
    print(TARGET)


if __name__ == "__main__":
    main()
