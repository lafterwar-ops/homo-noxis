from pathlib import Path
import json
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[2]
TMP = Path(__file__).resolve().parent
OUT = ROOT / 'output' / 'documents' / 'Homo-Noxius-100-Question-Editorial-Questionnaire.docx'
data = json.loads((TMP / 'questions1-50.json').read_text(encoding='utf-8')) + json.loads((TMP / 'questions51-100.json').read_text(encoding='utf-8'))
assert [q['id'] for q in data] == list(range(1, 101))
assert all(len(q['options']) == 4 and q['question'].strip() for q in data)

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
sec.top_margin, sec.bottom_margin = Inches(.68), Inches(.65)
sec.left_margin = sec.right_margin = Inches(.78)
sec.header_distance = sec.footer_distance = Inches(.3)
for name in ['Normal', 'Title', 'Subtitle', 'Heading 1', 'Heading 2']:
    style = doc.styles[name]
    style.font.name = 'Arial'
    style.font.color.rgb = RGBColor(0, 0, 0)
    style._element.get_or_add_rPr().rFonts.set(qn('w:ascii'), 'Arial')
    style._element.rPr.rFonts.set(qn('w:hAnsi'), 'Arial')
normal = doc.styles['Normal']
normal.font.size = Pt(11)
normal.paragraph_format.line_spacing = 1.04
normal.paragraph_format.space_after = Pt(4)
doc.styles['Title'].font.size = Pt(26)
doc.styles['Title'].paragraph_format.space_after = Pt(10)
doc.styles['Subtitle'].font.size = Pt(14)
doc.styles['Heading 1'].font.size = Pt(13)
doc.styles['Heading 1'].paragraph_format.space_after = Pt(8)

foot = sec.footer.paragraphs[0]
foot.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r = foot.add_run('Homo Noxius  |  ')
r.font.size = Pt(9)
field = OxmlElement('w:fldSimple'); field.set(qn('w:instr'), 'PAGE')
foot._p.append(field)

doc.add_paragraph('Homo Noxius', 'Title')
doc.add_paragraph('100 question editorial questionnaire', 'Subtitle')
doc.add_paragraph('4 November 2026')
doc.add_paragraph('Complete this document offline and return the saved file when you have answered all 100 questions. Your answers will determine which proposed revisions we pursue, preserve or reject.')
doc.add_paragraph('How to answer', 'Heading 1')
for text in [
    'For each question, type A, B, C, D or E in the Answer field. All fields are blank; nothing is preselected.',
    'A is my recommendation. You can choose a different option without explanation, or select E and write your own answer in the field beneath it.',
    'You may also use the E field to qualify a selected option, combine choices, defer a decision or state that another answer makes this question inapplicable. The field expands as you type.',
    'The questions retain the numbering and choices from the chat questionnaire. Where a general decision and a specific answer conflict, I will flag the conflict rather than assume which one governs.',
    'Complete the file in Word or another compatible word processor, save it as a DOCX and attach that completed file in chat. Printing and handwriting your answers is also possible.'
]:
    doc.add_paragraph(text)
doc.add_paragraph('Scope', 'Heading 1')
doc.add_paragraph('Questions 1 to 5 set the revision mandate. Questions 6 to 90 address specific passages, mechanisms, character consequences and pacing. Questions 91 to 100 cover protected artistic choices, validation and the stopping condition.')
doc.add_paragraph('Preparing this questionnaire changes no manuscript text. Any implementation follows your decisions, including your answer to Question 1.')
doc.add_page_break()

def text_control(p, tag, prompt, multiline=False):
    sdt = OxmlElement('w:sdt')
    pr = OxmlElement('w:sdtPr')
    alias = OxmlElement('w:alias'); alias.set(qn('w:val'), tag); pr.append(alias)
    t = OxmlElement('w:tag'); t.set(qn('w:val'), tag); pr.append(t)
    sid = OxmlElement('w:id'); sid.set(qn('w:val'), str(10000 + len(doc.element.xpath('//w:sdt')))); pr.append(sid)
    typ = OxmlElement('w:text')
    if multiline: typ.set(qn('w:multiLine'), '1')
    pr.append(typ)
    ph = OxmlElement('w:showingPlcHdr'); pr.append(ph)
    sdt.append(pr)
    content = OxmlElement('w:sdtContent')
    run = OxmlElement('w:r')
    rpr = OxmlElement('w:rPr')
    color = OxmlElement('w:color'); color.set(qn('w:val'), '666666'); rpr.append(color)
    run.append(rpr)
    tx = OxmlElement('w:t'); tx.text = prompt; run.append(tx)
    content.append(run); sdt.append(content); p._p.append(sdt)

for index, q in enumerate(data):
    if index % 3 == 0:
        first, last = q['id'], min(q['id'] + 2, 100)
        doc.add_paragraph(f'Questions {first:03d} to {last:03d}' if first != last else f'Question {first:03d}', 'Heading 1')
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.keep_with_next = True
    p.add_run(f"{q['id']:03d}  {q['question']}").bold = True
    for letter, option in zip('ABCD', q['options']):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(.22)
        p.paragraph_format.first_line_indent = Inches(-.22)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        p.add_run(letter + '  ').bold = True
        p.add_run(option)
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    p.add_run('Answer  ').bold = True
    text_control(p, f"Q{q['id']:03d}_ANSWER", '[Type A, B, C, D or E]')
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(13)
    p.paragraph_format.keep_together = True
    p.add_run('E  Other or your own wording  ').bold = True
    text_control(p, f"Q{q['id']:03d}_TEXT", '[Write here if needed]', True)
    if index % 3 == 2 and index < 99:
        doc.add_page_break()

doc.core_properties.title = 'Homo Noxius 100 question editorial questionnaire'
doc.core_properties.subject = 'Offline author decisions for the manuscript revision'
doc.core_properties.author = 'OpenAI'
doc.core_properties.comments = ''
for root in [doc.styles.element, doc.element]:
    for border in root.xpath('//w:pBdr'):
        border.getparent().remove(border)
OUT.parent.mkdir(parents=True, exist_ok=True)
doc.save(OUT)
assert len(doc.element.xpath('//w:sdt')) == 200
print(f'Saved {OUT}')
print('Validated 100 questions, 400 listed choices, 100 custom-response fields, 100 answer fields.')
