#!/usr/bin/env python3
"""Steam-Analysis logo: a low oak chest straight on, iron bands crossing its lid,
a hasp hanging open because the piece inside has just been lifted out. Body in
roman red darkened toward umber, bands and corner plates in dull bronze, one
pale marble white highlight along the lid edge. Wordmark below in Astloch,
bronze ink, packed close. At 64px the lettering drops and chest, bands, and
hasp carry the mark alone."""
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np
W = H = 1024
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
RED = (138, 46, 36); RED_D = (104, 34, 27); BRONZE = (150, 110, 60); IRON = (52, 48, 42)
img = Image.new("RGB", (W, H), (238, 230, 214)); d = ImageDraw.Draw(img, "RGBA")
x0, y0, x1, y1 = 132, 190, 892, 640
# lid: shallow dome band
d.polygon([(x0, y0 + 92), (x1, y0 + 92), (x1 - 64, y0), (x0 + 64, y0)], fill=RED_D)
d.line([(x0 + 64, y0 + 4), (x1 - 64, y0 + 4)], fill=(244, 238, 224), width=10)  # marble white lid edge highlight
d.rectangle([x0, y0 + 92, x1, y1], fill=RED)
d.line([(x0, y0 + 92), (x1, y0 + 92)], fill=(70, 26, 20), width=6)
bw = 14 if v == "v1" else 26
for bx in (x0 + 96, (x0 + x1) // 2 - bw // 2, x1 - 96 - bw):
    d.polygon([(bx + 10, y0 + 8), (bx + bw - 10, y0 + 8), (bx + bw, y0 + 92), (bx, y0 + 92)], fill=IRON)
    d.rectangle([bx, y0 + 92, bx + bw, y1], fill=IRON)
    d.rectangle([bx, y0 + 92, bx + bw, y1], outline=BRONZE, width=2)
for cx, cy in ((x0, y0 + 92), (x1 - 44, y0 + 92), (x0, y1 - 44), (x1 - 44, y1 - 44)):
    d.rectangle([cx, cy, cx + 44, cy + 44], fill=BRONZE)  # corner plates
# hasp hanging open, swung down from the lid seam at centre
hx = (x0 + x1) // 2
d.rectangle([hx - 17, y0 + 92, hx + 17, y0 + 150], fill=BRONZE)
d.polygon([(hx - 24, y0 + 148), (hx + 24, y0 + 148), (hx + 10, y0 + 226), (hx - 34, y0 + 218)], fill=(96, 72, 38))
d.ellipse([hx - 13, y0 + 186, hx + 13, y0 + 212], outline=(30, 28, 24), width=6)
if v != "v1":
    f = ImageFont.truetype("fonts/Astloch.ttf", 92)
    txt = "Steam-Analysis"; tw = d.textlength(txt, font=f)
    d.text(((W - tw) / 2, 716), txt, font=f, fill=(122, 84, 38))
rng = np.random.default_rng(3); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "logo.png" if v == "ship" else f"scratch/logo-{v}.png"
img.save(out); print(out)
img.resize((64, 64), Image.LANCZOS).save(f"scratch/logo64-{v}.png"); print("64px saved")
