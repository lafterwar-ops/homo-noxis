from pathlib import Path
import json
from pypdf import PdfReader
from PIL import Image, ImageOps, ImageDraw

root = Path(__file__).resolve().parent
pdf = root / "Homo-Noxius-Chapters-1-3.pdf"
reader = PdfReader(pdf)
texts = [page.extract_text() or "" for page in reader.pages]
ending = "before I take the next of it."
assert ending in texts[-1], texts[-1][-1000:]
assert not any("Chapter 4" in text or "CHAPTER 4" in text for text in texts)
pages = sorted((root / "render").glob("page-*.png"))
assert len(pages) == len(reader.pages), (len(pages), len(reader.pages))
for start in range(0, len(pages), 12):
    sheet = Image.new("RGB", (1600, 1860), "#dddddd")
    draw = ImageDraw.Draw(sheet)
    for slot, path in enumerate(pages[start:start + 12]):
        image = Image.open(path).convert("RGB")
        image.thumbnail((380, 570), Image.Resampling.LANCZOS)
        x = (slot % 4) * 400 + (400 - image.width) // 2
        y = (slot // 4) * 620 + 30
        sheet.paste(image, (x, y))
        draw.text(((slot % 4) * 400 + 12, (slot // 4) * 620 + 10), f"PAGE {start + slot + 1}", fill="black")
    sheet.save(root / f"contact-{start + 1:02d}-{min(start + 12, len(pages)):02d}.jpg", quality=92)
print(json.dumps({
    "pages": len(reader.pages),
    "chapter_openings": [{"page": i + 1, "text": t[:160]} for i, t in enumerate(texts) if "CHAPTER" in t[:160] or "Chapter" in t[:160]],
    "last_page": texts[-1],
    "blank_pages": [i + 1 for i, t in enumerate(texts) if not t.strip()],
    "sheets": [str(p) for p in sorted(root.glob("contact-*.jpg"))],
}, ensure_ascii=False))
