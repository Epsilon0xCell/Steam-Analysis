#!/usr/bin/env python3
"""Steam-Analysis intro banner: the guild hall before judgment, wordless.
Foreground: oak judging table with a closed iron banded chest and a folded cap.
Middle: empty benches, a vacant raised chair, a low brazier by a barred door.
Far: stone walls, one slit window with an amber shaft and dust, boot prints
in the dust leading from the door to the table and stopping there.
No text, letters, marks, or symbols anywhere."""
import sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
W, H = 1600, 900
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
AMBER = (232, 168, 74); BRONZE = (148, 108, 58); RED = (142, 44, 34)
CYPRESS = (26, 34, 28); WOOD = (92, 62, 36); WOOD_D = (58, 38, 20)
img = Image.new("RGB", (W, H), (104, 94, 82)); d = ImageDraw.Draw(img, "RGBA")
# stone wall with block courses
for y in range(0, 620, 78):
    d.line([(0, y), (W, y)], fill=(84, 74, 62), width=3)
    off = 90 if (y // 78) % 2 else 0
    for x in range(off, W, 190):
        d.line([(x, y), (x, y + 78)], fill=(84, 74, 62), width=3)
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(0, 0, 0, int(70 * t)), width=1)
# floor boards in cypress shadow
d.rectangle([0, 620, W, H], fill=(44, 36, 26))
for x in range(0, W, 130):
    d.line([(x - 200, 900), (x + 260, 620)], fill=(30, 24, 16), width=4)
# slit window high left and its amber shaft
d.rectangle([168, 70, 232, 300], fill=(20, 18, 14)); d.rectangle([178, 80, 222, 290], fill=(250, 196, 104))
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
shaft_a = 52 if v == "v1" else 78
ld.polygon([(190, 290), (228, 290), (760, 700), (430, 700)], fill=(255, 190, 92, shaft_a))
img = Image.alpha_composite(img.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(18))).convert("RGB")
d = ImageDraw.Draw(img, "RGBA")
rng = np.random.default_rng(11)
for _ in range(46):  # dust inside the shaft
    t = rng.random(); x = 200 + t * 480 + rng.normal(0, 26); y = 300 + t * 380
    d.ellipse([x, y, x + 4, y + 4], fill=(255, 220, 150, 170))
# other windows shuttered
for wx in (1150, 1330):
    d.rectangle([wx, 90, wx + 110, 300], fill=(52, 40, 26))
    for sy in range(110, 290, 36):
        d.line([(wx + 8, sy), (wx + 102, sy)], fill=(34, 26, 16), width=5)
# barred heavy door, right
d.rectangle([1408, 260, 1568, 700], fill=(62, 42, 24))
for px in range(1420, 1560, 34):
    d.line([(px, 268), (px, 692)], fill=(44, 29, 15), width=5)
d.rectangle([1400, 420, 1576, 452], fill=(30, 28, 26))  # the bar
d.rectangle([1400, 540, 1576, 566], fill=(30, 28, 26))
# vacant raised chair against far wall, centre right: high back, seat, arms, steps
cx = 920
d.rectangle([cx, 210, cx+170, 470], fill=(74,48,26))
d.rectangle([cx+16, 226, cx+154, 380], fill=(90,58,32))
d.polygon([(cx-6,210),(cx+176,210),(cx+85,158)], fill=WOOD_D)
d.rectangle([cx+16, 380, cx+154, 420], fill=RED)  # seat cushion
for lx in (cx+6, cx+146):
    d.rectangle([lx, 420, lx+18, 540], fill=WOOD_D)
    d.rectangle([lx-8, 348, lx+26, 366], fill=WOOD_D)  # arm rests
d.rectangle([cx-14, 528, cx+184, 550], fill=WOOD_D)
d.rectangle([cx+8, 550, cx+162, 570], fill=(48,31,16))  # lower step
# empty benches facing the table, two broken rows with a centre aisle
for by, tone in ((486,(70,48,28)),(560,(56,38,21))):
    for bx,bw in ((70,560),(990,540)):
        d.rectangle([bx, by, bx+bw, by+20], fill=tone)
        d.rectangle([bx, by-40, bx+bw, by-24], fill=tone)
        for lx in (bx+36, bx+bw//2, bx+bw-48):
            d.rectangle([lx, by-24, lx+12, by+58], fill=tuple(max(0,c-12) for c in tone))
# brazier low near the door, smoke rising straight
bx, by = 1245, 648
d.polygon([(bx - 52, by), (bx + 52, by), (bx + 26, by + 34), (bx - 26, by + 34)], fill=(38, 34, 30))
for lx in (-34, 0, 34):
    d.line([(bx + lx // 2, by + 30), (bx + lx, by + 78)], fill=(30, 27, 24), width=6)
glow = 120 if v == "v1" else 185
d.ellipse([bx - 40, by - 14, bx + 40, by + 8], fill=(214, 96, 36, glow))
d.ellipse([bx - 18, by - 10, bx + 18, by + 4], fill=(250, 178, 84, 220))
smoke = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(smoke)
for i in range(9):
    sx = bx + (i % 3 - 1) * 7; sy = by - 60 - i * 44; r = 16 + i * 7
    sd.ellipse([sx - r, sy - r // 2, sx + r, sy + r // 2], fill=(190, 186, 178, 52))
img = Image.alpha_composite(img.convert("RGBA"), smoke.filter(ImageFilter.GaussianBlur(10))).convert("RGB")
d = ImageDraw.Draw(img, "RGBA")
# judging table fills the lower third
d.rectangle([90, 690, 1510, 726], fill=(104, 70, 38))
d.rectangle([90, 690, 1510, 702], fill=(128, 88, 48))
for lx in (150, 1420):
    d.rectangle([lx, 726, lx + 34, 880], fill=WOOD_D)
d.rectangle([90, 848, 1510, 880], fill=(40, 27, 15))
for sx in range(140, 1480, 90):  # scars on the table top
    d.line([(sx, 696), (sx + 34, 700)], fill=(70, 46, 22), width=2)
# closed chest with iron bands on the table
tx, ty, tw, th = 520, 520, 470, 172
d.polygon([(tx, ty + 44), (tx + tw, ty + 44), (tx + tw - 52, ty - 46), (tx + 52, ty - 46)], fill=(128, 52, 40))
d.rectangle([tx, ty + 44, tx + tw, ty + th], fill=RED)
d.line([(tx + 52, ty - 46), (tx + tw - 52, ty - 46)], fill=(238, 226, 200), width=5)  # pale lid edge in the shaft light
for bx2 in (tx + 84, tx + tw // 2 - 13, tx + tw - 110):
    d.rectangle([bx2, ty - 42, bx2 + 26, ty + th], fill=(52, 46, 40))
    d.rectangle([bx2, ty - 42, bx2 + 26, ty + th], outline=BRONZE, width=2)
d.rectangle([tx + tw // 2 - 30, ty + 60, tx + tw // 2 + 30, ty + 118], fill=(66, 56, 44))
d.rectangle([tx + tw // 2 - 12, ty + 76, tx + tw // 2 + 12, ty + 104], fill=(26, 24, 22))  # shut hasp plate
# folded cap left beside the chest
d.polygon([(300, 668), (452, 668), (420, 622), (330, 622)], fill=(48, 52, 44))
d.polygon([(300, 668), (452, 668), (438, 684), (314, 684)], fill=(34, 37, 31))
# boot prints in the dust: flat pale pairs on the floor plane, door to table, stopping
def boot(x, y, s, a):
    d.ellipse([x, y, x+34*s, y+13*s], fill=(198,180,150, a))
    d.ellipse([x+6*s, y+14*s, x+26*s, y+22*s], fill=(198,180,150, a))
boot(1420, 724, 1.0, 130); boot(1452, 744, 1.0, 135)
boot(1310, 736, 1.05, 145); boot(1344, 758, 1.05, 150)
boot(1196, 748, 1.1, 160); boot(1230, 772, 1.1, 168)
boot(1082, 762, 1.15, 178)
a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "intro-banner.png" if v == "ship" else f"scratch/intro-{v}.png"
img.save(out); print(out)
