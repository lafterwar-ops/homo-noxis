from pathlib import Path
from PIL import Image, ImageDraw

folder = Path(__file__).parent
pages = sorted(folder.glob('page-*.png'))
cell_w, cell_h = 660, 985
for start in range(0, len(pages), 4):
    sheet = Image.new('RGB', (cell_w * 2, cell_h * 2), '#e8e8e8')
    draw = ImageDraw.Draw(sheet)
    for offset, path in enumerate(pages[start:start + 4]):
        page = Image.open(path).convert('RGB')
        page.thumbnail((cell_w - 12, cell_h - 32), Image.Resampling.LANCZOS)
        x = (offset % 2) * cell_w + (cell_w - page.width) // 2
        y = (offset // 2) * cell_h + 25
        sheet.paste(page, (x, y))
        draw.text(((offset % 2) * cell_w + 14, (offset // 2) * cell_h + 6), path.stem, fill='black')
    out = folder / f'contact-{start // 4 + 1}.jpg'
    sheet.save(out, quality=78)
    print(out.name, out.stat().st_size)
