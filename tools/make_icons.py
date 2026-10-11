"""Genera le icone della PWA: fiamma pixel (forma del cursore dell'intensità) su fondo bg.
Uso: python3 tools/make_icons.py  -> docs/icons/*.png"""
import zlib, struct, re, os

PATH = ('M8.8 1C11 3.6 13.6 5 15.5 6.9C17.9 9.3 19.2 11.9 18.8 15.2C18.6 17.4 17.6 19 16.4 20.4C18.2 20.4 19.8 19.2 20.6 17.2'
        'C22.8 19.4 23.4 23.2 22.2 26.2C20.6 29.8 16.8 31.4 12 31.4C6 31.4 1.2 27.6 1.2 22.2C1.2 19 2.2 16.4 3.6 14.4'
        'C4.2 16.6 5.8 18.4 7.8 18.4C9.8 18.4 10.8 16.8 10.2 14.6C9.6 12.4 7.4 10.8 7.2 7.6C7 5 7.6 2.8 8.8 1Z')
BG = (12, 10, 9)
TONES = [(191, 71, 7), (226, 86, 26), (207, 135, 23), (239, 239, 199)]   # bordo -> cuore

def polygon():
    nums = list(map(float, re.findall(r'-?\d+\.?\d*', PATH)))
    x, y = nums[0], nums[1]; pts = [(x, y)]; i = 2
    while i + 5 < len(nums):
        x1, y1, x2, y2, x3, y3 = nums[i:i + 6]; i += 6
        for k in range(1, 17):
            t = k / 16; u = 1 - t
            pts.append((u**3*x + 3*u*u*t*x1 + 3*u*t*t*x2 + t**3*x3, u**3*y + 3*u*u*t*y1 + 3*u*t*t*y2 + t**3*y3))
        x, y = x3, y3
    return pts

def inside(pts, px, py):
    c = False
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        if (y1 > py) != (y2 > py) and px < (x2 - x1) * (py - y1) / (y2 - y1) + x1: c = not c
    return c

def flame_grid(cols=12, rows=16):
    pts = polygon()
    g = [[inside(pts, 1 + (c + 0.5) * 22 / cols, 1 + (r + 0.5) * 30.4 / rows) for c in range(cols)] for r in range(rows)]
    lvl = [[-1 if not g[r][c] else 0 for c in range(cols)] for r in range(rows)]
    for L in range(1, 4):   # erosione: più lontano dal bordo = più caldo
        for r in range(rows):
            for c in range(cols):
                if lvl[r][c] == L - 1 and all(0 <= r + dr < rows and 0 <= c + dc < cols and lvl[r + dr][c + dc] >= L - 1
                                               for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    lvl[r][c] = L
    return lvl

def png(path, size, pad_cells):
    lvl = flame_grid(); rows, cols = len(lvl), len(lvl[0])
    grid = rows + 2 * pad_cells; cell = size / grid
    ox = (grid - cols) / 2; oy = pad_cells
    raw = bytearray()
    for y in range(size):
        raw.append(0)
        gy = int(y / cell - oy)
        for x in range(size):
            gx = int(x / cell - ox) if x / cell - ox >= 0 else -1
            col = BG
            if 0 <= gy < rows and 0 <= gx < cols and lvl[gy][gx] >= 0: col = TONES[min(lvl[gy][gx], 3)]
            raw += bytes(col)
    def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    data = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(bytes(raw), 9)) + chunk(b'IEND', b'')
    open(path, 'wb').write(data)

os.makedirs('docs/icons', exist_ok=True)
for name, size, pad in [('icon-192.png', 192, 3), ('icon-512.png', 512, 3), ('icon-maskable-512.png', 512, 6),
                        ('apple-touch-icon.png', 180, 3), ('favicon-32.png', 32, 1)]:
    png(f'docs/icons/{name}', size, pad)
print('ok')
