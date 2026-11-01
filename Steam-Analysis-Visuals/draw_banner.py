#!/usr/bin/env python3
"""Steam-Analysis wordmark banner: guild hall interior, the long judging table
across the width, the opened chest and the single written sheet weighted by a
bronze seal ring, three older judges standing behind the table with hands
folded, a younger candidate on the near side with cap in hands and eyes on the
sheet, empty side benches, one amber bar from a high left window, and the name
Steam-Analysis cut into the beam above the table in Astloch, limewashed pale."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
W, H = 2560, 640
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
RED = (138, 46, 36); BRONZE = (150, 110, 60); WHITE = (244, 238, 224); GOWN = (44, 40, 38)
img = Image.new("RGB", (W, H), (96, 84, 70)); d = ImageDraw.Draw(img, "RGBA")
for y in range(0, H, 64):
    d.line([(0, y), (W, y)], fill=(78, 68, 56), width=3)
d.rectangle([0, 470, W, H], fill=(46, 36, 24))
# high window left, amber bar across the table
d.rectangle([120, 40, 190, 210], fill=(250, 196, 104))
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
ld.polygon([(150, 210), (196, 210), (1060, 500), (560, 500)], fill=(255, 190, 92, 64))
img = Image.alpha_composite(img.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(14))).convert("RGB")
d = ImageDraw.Draw(img, "RGBA")
# beam above the table carrying the cut name
d.rectangle([180, 96, 2380, 196], fill=(74, 50, 26))
d.rectangle([180, 96, 2380, 108], fill=(96, 66, 34))
f = ImageFont.truetype("fonts/Astloch.ttf", 92 if v == "ship" else 64)
txt = "Steam-Analysis"; tw = d.textlength(txt, font=f)
d.text(((W - tw) / 2, 100), txt, font=f, fill=(232, 226, 198))
# side benches, empty
for bx in (60, 2060):
    d.rectangle([bx, 400, bx + 440, 420], fill=(66, 46, 26))
    for lx in (bx + 30, bx + 380):
        d.rectangle([lx, 420, lx + 16, 500], fill=(50, 34, 18))
# three judges behind the table, gowns, folded hands, heads bowed a fraction
for jx, tone in ((880, GOWN), (1180, (54, 46, 40)), (1480, GOWN)):
    d.polygon([(jx - 78, 470), (jx + 78, 470), (jx + 52, 268), (jx - 52, 268)], fill=tone)
    d.ellipse([jx - 30, 196, jx + 30, 262], fill=(198, 164, 128))
    d.polygon([(jx - 34, 208), (jx + 34, 208), (jx + 20, 182), (jx - 20, 182)], fill=(210, 206, 196))  # grey hair cap
    d.polygon([(jx - 40, 356), (jx, 392), (jx + 40, 356), (jx + 26, 336), (jx, 364), (jx - 26, 336)], fill=(188, 154, 118))  # folded hands
# judging table across the width
d.rectangle([240, 470, 2320, 506], fill=(116, 78, 40)); d.rectangle([240, 470, 2320, 482], fill=(140, 96, 50))
for lx in (320, 2180):
    d.rectangle([lx, 506, lx + 36, 620], fill=(62, 42, 22))
# opened chest on the table, lid raised back
tx, ty = 620, 356
d.rectangle([tx, ty + 60, tx + 330, ty + 114], fill=RED)
d.polygon([(tx, ty + 60), (tx + 330, ty + 60), (tx + 290, ty - 58), (tx + 40, ty - 58)], fill=(104, 34, 27))
for bx in (tx + 52, tx + 262):
    d.rectangle([bx, ty - 54, bx + 20, ty + 114], fill=(52, 48, 42))
d.rectangle([tx + 20, ty + 72, tx + 310, ty + 104], fill=(226, 218, 196))  # empty inside, pale lining
# the single written sheet, weighted by the seal ring
sx, sy = 1180, 402
d.polygon([(sx, sy), (sx + 330, sy - 8), (sx + 338, sy + 62), (sx + 8, sy + 70)], fill=WHITE)
for ly in range(sy + 14, sy + 56, 13):
    d.line([(sx + 22, ly), (sx + 290, ly - 6)], fill=(168, 160, 146), width=3)
ring_r = 40 if v == "ship" else 26
d.ellipse([sx + 236, sy - 2, sx + 236 + ring_r * 2, sy - 2 + ring_r * 2], outline=BRONZE, width=10)
d.ellipse([sx + 236 + ring_r - 7, sy - 2 + ring_r - 7, sx + 236 + ring_r + 7, sy - 2 + ring_r + 7], fill=(120, 84, 40))
# candidate on the near side, cap in hands, eyes on the sheet (back three-quarter)
kx = 1980
d.polygon([(kx - 70, 640), (kx + 76, 640), (kx + 50, 420), (kx - 48, 420)], fill=(86, 62, 40))
d.ellipse([kx - 28, 348, kx + 32, 414], fill=(198, 164, 128))
d.polygon([(kx - 52, 500), (kx - 6, 522), (kx - 24, 548), (kx - 62, 528)], fill=(188, 154, 118))
d.polygon([(kx - 66, 520), (kx - 2, 544), (kx - 14, 566), (kx - 70, 544)], fill=(48, 52, 44))  # the cap, held
rng = np.random.default_rng(5); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "banner.png" if v == "ship" else f"scratch/banner-{v}.png"
img.save(out); print(out)
