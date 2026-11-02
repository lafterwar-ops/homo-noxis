from pathlib import Path
import subprocess
import json
from PIL import Image, ImageOps, ImageDraw

here = Path(__file__).resolve().parent
root = here.parents[2]
pdf = root / "output/pdf/La-pilule-Sith-contre-les-boomers-FR.pdf"
render = here / "render"
render.mkdir(exist_ok=True)
poppler = Path("C:/Users/Multiple Monitors/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe")
subprocess.run([str(poppler), "-r", "90", "-png", str(pdf), str(render / "page")], check=True)
page_count = json.loads((here / "validation.json").read_text(encoding="utf-8"))["pages"]
pages = [render / f"page-{index:02d}.png" for index in range(1, page_count+1)]
assert all(page.exists() for page in pages)
for offset in range(0, len(pages), 9):
    sheet = Image.new("RGB", (930, 1344), "#E1E4E6")
    draw = ImageDraw.Draw(sheet)
    for slot, page in enumerate(pages[offset:offset+9]):
        thumb = ImageOps.contain(Image.open(page).convert("RGB"), (290, 410))
        x = (slot % 3) * 310 + 10
        y = (slot // 3) * 448 + 23
        draw.text((x, y-17), str(offset + slot + 1), fill="#30363B")
        sheet.paste(thumb, (x, y))
    target = render / f"overview-{offset//9+1}.png"
    sheet.save(target)
    print(target)
print(f"Rendered {len(pages)} pages")
