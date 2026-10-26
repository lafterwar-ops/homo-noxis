from pathlib import Path
import hashlib, json, re, subprocess, shutil
from pypdf import PdfReader
from PIL import Image, ImageOps, ImageDraw

root = Path(r"C:/Francois/Writting/HomoNoxisGithub")
work = root / "tmp/pdfs/2026-10-16-chapter18"
pdf = work / "Homo-Noxius-Chapter-18-Return.pdf"
reader = PdfReader(str(pdf))
texts = [page.extract_text() or "" for page in reader.pages]
whole = re.sub(r"\s+", " ", " ".join(texts))
checks = [
    "I need your account of the hearing.",
    "My name is Alice, and I remember everything.",
    "Your Mountain may call this its wall.",
    "That is what the division is meant to prevent.",
    "The smell remained for twelve steps more.",
    "We ran after the others.",
]
compact = re.sub(r"\s+", "", whole)
missing = [s for s in checks if re.sub(r"\s+", "", s) not in compact]
assert not missing, missing
assert not any("Chapter 19" in t for t in texts), "Unexpected following chapter"
assert all(t.strip() for t in texts), "Blank page"
for p, page in enumerate(reader.pages, 1):
    assert abs(float(page.mediabox.width) - 432) < 1
    assert abs(float(page.mediabox.height) - 648) < 1
render = work / "render"
render.mkdir(exist_ok=True)
subprocess.run(["pdftoppm", "-r", "90", "-png", str(pdf), str(render / "page")], check=True)
images = sorted(render.glob("page-*.png"))
assert len(images) == len(reader.pages)
for start in range(0, len(images), 4):
    selected = images[start:start+4]
    sheet = Image.new("RGB", (1080, 1680), "#dddddd")
    draw = ImageDraw.Draw(sheet)
    for j, file in enumerate(selected):
        page = Image.open(file).convert("RGB")
        page.thumbnail((520, 780))
        x = (j % 2) * 540 + (540 - page.width) // 2
        y = (j // 2) * 830 + 24
        x = (j % 2) * 540 + (540 - page.width) // 2
        sheet.paste(page, (x, y))
        draw.text(((j % 2)*540+10, (j//2)*830+7), f"Page {start+j+1}", fill="black")
    sheet.save(work / f"contact-{start+1:02d}-{start+len(selected):02d}.jpg", quality=88)
print(json.dumps({"pages": len(reader.pages), "checks": checks, "first_page": texts[0], "last_page": texts[-1], "contacts": [str(p) for p in sorted(work.glob("contact-*.jpg"))]}, ensure_ascii=False))
