from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size, path):
    img = Image.new('RGBA', (size, size), (26, 23, 48, 255))
    draw = ImageDraw.Draw(img)

    pad = size * 0.18
    s = size - pad * 2
    x0, y0 = pad, pad
    x1, y1 = pad + s, pad + s

    # Border radius approx
    r = size * 0.22
    draw.rounded_rectangle([x0, y0, x1, y1], radius=r,
                            fill=(44, 39, 72, 255),
                            outline=(124, 111, 247, 100), width=max(1, int(size*0.02)))

    # Window cross
    cx, cy = size / 2, size / 2
    lw = max(1, int(size * 0.04))
    col = (166, 155, 255, 255)

    # Outer rect
    m = size * 0.26
    draw.rounded_rectangle([m, m, size-m, size-m], radius=size*0.08,
                            outline=col, width=lw, fill=None)
    # Vertical line
    draw.line([(cx, m), (cx, size-m)], fill=col, width=lw)
    # Horizontal line
    draw.line([(m, cy), (size-m, cy)], fill=col, width=lw)

    # Dots
    dot = max(2, int(size * 0.05))
    dot_col = (166, 155, 255, 255)
    qx, qy = (m + cx) / 2, (m + cy) / 2
    draw.ellipse([qx-dot, qy-dot, qx+dot, qy+dot], fill=dot_col)
    qx2 = (cx + size-m) / 2
    draw.ellipse([qx2-dot, qy-dot, qx2+dot, qy+dot], fill=dot_col)

    img.save(path)
    print(f"  ✓ {path} ({size}×{size})")

os.makedirs('/home/claude/ventanas-p65-mobile/static', exist_ok=True)
make_icon(192, '/home/claude/ventanas-p65-mobile/static/icon-192.png')
make_icon(512, '/home/claude/ventanas-p65-mobile/static/icon-512.png')
print("Icons generated!")
