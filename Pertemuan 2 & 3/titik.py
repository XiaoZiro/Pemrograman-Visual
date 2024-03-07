import numpy as np
import matplotlib.pyplot as plt

# user entries
x1 = 100; y1 = 200
x2 = 500; y2 = 500

# the user decides the line width
lw = int(10)
hw = int(lw/2)

col = int(800)
row = int(800)
print('col, row = ', col, '', row)

# Preparing the black canvas
Gambar = np.zeros(shape=(row, col,3), dtype = np.uint8)
Gambar[:,:,:] = 255

# menggambar titik dengan stu piksel
Gambar[y1,x1,:] =0
Gambar[y2,x2,:] =0
Gambar[y1,x1,:] = 255
Gambar[y2,x2,:] = 255

# coloring the two points red
for i in range(x1-hw, x1+hw):
    for j in range(y1-hw, y1+hw):
        if((i-x1)**2 + (j-y1)**2) < hw**2:
            Gambar[j,i,:] =0
            Gambar[j,i,0] = 255

# coloring the two points red
for i in range(x2-hw, x2+hw):
    for j in range(y2-hw, y2+hw):
        if((i-x2)**2 + (j-y2)**2) < hw**2:
            Gambar[j,i,:] =0
            Gambar[j,i,0] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()