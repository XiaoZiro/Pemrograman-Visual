import numpy as np
import matplotlib.pyplot as plt

rowmax = int(1000)
colmax = int(1000)

Gambar = np.zeros(shape=(rowmax+1, colmax+1, 3), dtype=np.int16)

# Membuat segitiga besar
for i in range(0, rowmax+1):
    for j in range(0, colmax+1):
        if i >= j and i <= rowmax - j:
            Gambar[i, j, 0] = 255  # Warna merah untuk segitiga atas
        elif i >= rowmax - j and i <= j:
            Gambar[i, j, 1] = 255  # Warna hijau untuk segitiga bawah
        elif i <= rowmax - j and i <= j:
            Gambar[i, j, 2] = 255  # Warna biru untuk segitiga kiri

# # Membuat segitiga dalam 1 (merah)
# for i in range(rowmax//4, rowmax*3//4 + 1):
#     for j in range(colmax//4, rowmax//2 - i//2 + colmax//2 + 1):
#         Gambar[i, j, 0] = 255
#
# # Membuat segitiga dalam 2 (hijau)
# for i in range(rowmax//4, rowmax*3//4 + 1):
#     for j in range(colmax//2, -i//2 + colmax//2 + 1, -1):
#         Gambar[i, j, 1] = 255
#
# # Membuat segitiga dalam 3 (biru)
# for i in range(rowmax*3//4, rowmax//4 - 1, -1):
#     for j in range(colmax//4, rowmax//2 - i//2 + colmax//2 + 1):
#         Gambar[i, j, 2] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()
