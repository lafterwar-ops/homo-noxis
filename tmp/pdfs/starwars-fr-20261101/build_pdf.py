from pathlib import Path
import json
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from pypdf import PdfReader
import pdfplumber


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUTPUT = ROOT / "output" / "pdf" / "La-pilule-Sith-contre-les-boomers-FR.pdf"
SOURCE = json.loads((HERE / "source-paragraphs.json").read_text(encoding="utf-8-sig"))

translations = []
for part in range(1, 4):
    translations.extend(json.loads((HERE / f"fr-part{part}.json").read_text(encoding="utf-8-sig")))
translations.sort(key=lambda item: item["id"])
assert [item["id"] for item in translations] == list(range(4, 105)), "Missing or repeated paragraph"
assert len(SOURCE) == 105
for item in translations:
    assert item["text"].strip(), item["id"]
    assert not re.search(r"\b(?:TODO|PLACEHOLDER|TRANSLATE)\b", item["text"]), item["id"]
    assert not re.search(r"[\u2010-\u2015]", item["text"]), f"Non-ASCII dash in paragraph {item['id']}"

font_dir = Path("C:/Windows/Fonts")
for name, filename in (
    ("Georgia", "georgia.ttf"),
    ("Georgia-Bold", "georgiab.ttf"),
    ("Georgia-Italic", "georgiai.ttf"),
    ("Georgia-BoldItalic", "georgiaz.ttf"),
    ("Calibri", "calibri.ttf"),
    ("Calibri-Bold", "calibrib.ttf"),
):
    pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
pdfmetrics.registerFontFamily("Georgia", normal="Georgia", bold="Georgia-Bold", italic="Georgia-Italic", boldItalic="Georgia-BoldItalic")

ink = colors.HexColor("#20262C")
muted = colors.HexColor("#626A71")
accent = colors.HexColor("#7F4137")

body_style = ParagraphStyle(
    "Body", fontName="Georgia", fontSize=11, leading=15.7,
    textColor=ink, alignment=TA_JUSTIFY, spaceAfter=8.7,
    allowWidows=0, allowOrphans=0, splitLongWords=0,
)
quote_style = ParagraphStyle(
    "Quote", parent=body_style, fontName="Georgia-Italic",
    leftIndent=12, rightIndent=12, spaceBefore=4, spaceAfter=10,
    alignment=TA_LEFT, keepWithNext=True,
)
label_style = ParagraphStyle("Label", fontName="Calibri-Bold", fontSize=9, leading=12, textColor=accent, spaceAfter=12)
title_style = ParagraphStyle("Title", fontName="Georgia-Bold", fontSize=27, leading=32, textColor=ink, spaceAfter=13)
subtitle_style = ParagraphStyle("Subtitle", fontName="Georgia-Italic", fontSize=12.5, leading=18, textColor=muted, spaceAfter=17)
author_style = ParagraphStyle("Author", fontName="Calibri-Bold", fontSize=11, leading=15, textColor=ink, spaceAfter=3)
metadata_style = ParagraphStyle("Metadata", fontName="Calibri", fontSize=9, leading=12, textColor=muted, spaceAfter=12)
note_style = ParagraphStyle("Note", fontName="Calibri", fontSize=8.5, leading=11.5, textColor=muted, spaceAfter=20)
ending_style = ParagraphStyle("Ending", parent=body_style, fontName="Georgia-Bold", spaceBefore=2, alignment=TA_LEFT)


def markup(text):
    # Keep French quotation and punctuation clusters together without changing words.
    text = re.sub(r"«\s*", "«\u00a0", text)
    text = re.sub(r"\s*»", "\u00a0»", text)
    text = re.sub(r"[ \u00a0]+([;:?!])", "\u00a0\\1", text)
    return escape(text)


def furniture(canvas, doc):
    canvas.saveState()
    width, height = A4
    left = 26 * mm
    right = width - 26 * mm
    if doc.page > 1:
        canvas.setFont("Calibri", 8)
        canvas.setFillColor(muted)
        canvas.drawString(left, height - 17 * mm, "LA PILULE SITH CONTRE LES BOOMERS")
        canvas.setStrokeColor(colors.HexColor("#D6D9DC"))
        canvas.setLineWidth(0.4)
        canvas.line(left, height - 20 * mm, right, height - 20 * mm)
    canvas.setFont("Calibri", 8)
    canvas.setFillColor(muted)
    canvas.drawString(left, 15 * mm, "Upper Canadian Cavalier  |  Traduction française")
    canvas.drawRightString(right, 15 * mm, str(doc.page))
    canvas.restoreState()


story = [
    Paragraph("ESSAI  /  TRADUCTION FRANÇAISE", label_style),
    Paragraph("La pilule Sith<br/>contre les boomers", title_style),
    Paragraph("Comment Star Wars révèle la vision de l’histoire des boomers<br/>et prophétise sa fin", subtitle_style),
    Paragraph("Upper Canadian Cavalier", author_style),
    Paragraph("29 octobre 2026", metadata_style),
    Paragraph("Titre original : <i>Getting Sith-Pilled on the Boomers</i><br/>Traduction française non officielle du texte fourni. Les citations des films sont traduites depuis le texte anglais. Les affirmations sont celles de l’auteur.", note_style),
]
for item in translations:
    ident, text = item["id"], item["text"]
    if ident >= 103:
        continue
    style = quote_style if ident in (4, 6) else body_style
    story.append(Paragraph(markup(text), style))
story.append(KeepTogether([Paragraph(markup(item["text"]), ending_style) for item in translations if item["id"] >= 103]))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=A4, rightMargin=26 * mm, leftMargin=26 * mm,
    topMargin=26 * mm, bottomMargin=25 * mm,
    title="La pilule Sith contre les boomers", author="Upper Canadian Cavalier",
    subject="Traduction française intégrale de Getting Sith-Pilled on the Boomers",
    creator="Traduction française du texte fourni - mise en page PDF",
    pageCompression=1,
)
doc.build(story, onFirstPage=furniture, onLaterPages=furniture)

reader = PdfReader(str(OUTPUT))
geometry_issues = []
body_pages = []
with pdfplumber.open(OUTPUT) as pdf:
    for page_number, page in enumerate(pdf.pages, 1):
        body_pages.append(page.crop((0, 22 * mm, page.width, page.height - 23 * mm)).extract_text() or "")
        for char in page.chars:
            if char["x0"] < 0 or char["x1"] > page.width + 0.2 or char["top"] < 0 or char["bottom"] > page.height + 0.2:
                geometry_issues.append({"page": page_number, "text": char["text"]})
assert not geometry_issues, geometry_issues
normalize = lambda value: re.sub(r"\s+", "", value)
flat_pdf = normalize("\n".join(body_pages))
for item in translations:
    assert normalize(item["text"]) in flat_pdf, f"Missing text in PDF: paragraph {item['id']}"
report = {
    "output": str(OUTPUT), "pages": len(reader.pages),
    "translated_body_paragraphs": len(translations),
    "source_body_paragraphs": len(SOURCE) - 4,
    "french_body_words": sum(len(item["text"].split()) for item in translations),
    "every_paragraph_found_in_pdf": True,
    "off_page_characters": geometry_issues,
}
(HERE / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
