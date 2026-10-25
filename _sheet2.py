import os
from PIL import Image, ImageDraw
B = r"C:\Users\SCC1202201146\Documents\Ngoding\math-hero\public\assets\svg\craftpix\craftpix-net-396765-free-simple-platformer-game-kit-pixel-art"
OUT = r"C:\Users\SCC1202201146\Documents\Ngoding\math-hero\_sheet_out"

# Tileset dengan grid 16px dan label kolom/baris (skala 5x)
S = 5
im = Image.open(os.path.join(B, "7 Levels/Tiled/Tileset.png")).convert("RGBA")
W, H = im.width * S, im.height * S
c = Image.new("RGBA", (W + 20, H + 20), (60, 60, 80, 255))
c.alpha_composite(im.resize((W, H), Image.NEAREST), (20, 20))
d = ImageDraw.Draw(c)
for col in range(im.width // 16):
    d.line([(20 + col * 16 * S, 20), (20 + col * 16 * S, H + 20)], fill=(255, 0, 255, 160))
    d.text((24 + col * 16 * S, 4), str(col), fill=(255, 255, 0, 255))
for row in range(im.height // 16):
    d.line([(20, 20 + row * 16 * S), (W + 20, 20 + row * 16 * S)], fill=(255, 0, 255, 160))
    d.text((2, 24 + row * 16 * S), str(row), fill=(255, 255, 0, 255))
c.convert("RGB").save(os.path.join(OUT, "tileset_grid.png"))

# GUI: ikon, tombol, angka, interface (skala 3x)
def strip(paths, scale, per_row, label):
    ims = [Image.open(os.path.join(B, p)).convert("RGBA") for p in paths]
    cw = max(i.width for i in ims) * scale + 6
    ch = max(i.height for i in ims) * scale + 14
    rows = (len(ims) + per_row - 1) // per_row
    cv = Image.new("RGBA", (cw * per_row, ch * rows), (60, 60, 80, 255))
    dd = ImageDraw.Draw(cv)
    for k, i in enumerate(ims):
        x, y = (k % per_row) * cw, (k // per_row) * ch
        cv.alpha_composite(i.resize((i.width * scale, i.height * scale), Image.NEAREST), (x + 2, y + 12))
        dd.text((x + 2, y), str(k + 1), fill=(255, 255, 0, 255))
    return cv

icons = ["5 GUI/Icons/Icon_%02d.png" % k for k in range(1, 31)]
strip(icons, 4, 10, "icons").convert("RGB").save(os.path.join(OUT, "icons.png"))
btns = ["5 GUI/Buttons/Button_%02d.png" % k for k in range(1, 41)]
strip(btns, 2, 8, "btn").convert("RGB").save(os.path.join(OUT, "buttons.png"))
nums = ["5 GUI/Numbers/Number_%02d.png" % k for k in range(1, 51)]
strip(nums[:20], 3, 10, "num").convert("RGB").save(os.path.join(OUT, "numbers.png"))
for p in ["5 GUI/Text.png", "5 GUI/Palette.png"]:
    print(p, Image.open(os.path.join(B, p)).size)
print("ok")
