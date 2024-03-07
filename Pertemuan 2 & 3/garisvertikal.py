import numpy as np
import matplotlib.pyplot as plt

# titik
ya, xa = 200, 100
yb, xb = 1000, 100
yc, xc = 600, 600
yd, xd = 600, 200

# the user decide the point diameter and color
pd = int(8); pr = 255; pg = 0; pb = 255

# the user decide the line width and color
lw = int(8); lr = 0; lg = 255; lb = 255

# setting the size of the canvas
col, row = 800, 1200
print('col, row =', col,'', row)

# Function untuk membuat garis
def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd / 2)
    hw = int(lw / 2)
    dy = y2 - y1
    dx = x2 - x1

    # draw the first point
    for i in range(max(x1 - hd, 0), min(x1 + hd, col)):
        for j in range(max(y1 - hd, 0), min(y1 + hd, row)):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, 0] = 255
                Gambar[j, i, 1] = 255
                Gambar[j, i, 2] = 255

    # draw the second point
    for i in range(max(x2 - hd, 0), min(x2 + hd, col)):
        for j in range(max(y2 - hd, 0), min(y2 + hd, row)):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = 255
                Gambar[j, i, 1] = 255
                Gambar[j, i, 2] = 255

    # draw the line
    if abs(dy) <= abs(dx):  # untuk garis horizontal
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i - x1) + y1)
            for k in range(max(j - hw, 0), min(j + hw, row)):
                for l in range(max(i - hw, 0), min(i + hw, col)):
                    Gambar[k, l, 0] = lr
                    Gambar[k, l, 1] = lg
                    Gambar[k, l, 2] = lb

    else:  # untuk garis vertikal
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            for k in range(max(j - hw, 0), min(j + hw, row)):
                for l in range(max(i - hw, 0), min(i + hw, col)):
                    Gambar[k, l, 0] = lr
                    Gambar[k, l, 1] = lg
                    Gambar[k, l, 2] = lb

    return Gambar

### MAIN PROGRAM
hasil = buat_garis(ya, xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()
