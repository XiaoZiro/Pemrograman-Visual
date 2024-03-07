import numpy as np
import matplotlib.pyplot as plt

def hitung_gradien(y1, y2, x1, x2):
    return (y2 - y1) / (x2 - x1)

def rumus(x, y, gradient):
    return y - gradient * x

def line_plot(x1, y1, x2, y2):
    gradien = hitung_gradien(y1, y2, x1, x2)
    rumus1 = rumus(x1, y1, gradien)
    return gradien, rumus1

# Koordinat titik untuk Garis 1
x1 = 1
y1 = 2

# Koordinat titik untuk Garis 2
x2 = -3
y2 = 0
m1, c1 = line_plot(2, 0, 1, 2)

# Koordinat titik untuk Garis 1
x3 = 5
y3 = 6

# Koordinat titik untuk Garis 2
x4 = 2
y4 = 4
m2, c2 = line_plot(6, 4, 5, 2)

x = np.linspace(-10, 10, 1000)
y_values1 = m1 * x + c1
y_values2 = m2 * x + c2

plt.plot(x, y_values1, '-r', label='Garis 1')  # Warna merah untuk Garis 1
plt.plot(x, y_values2, '-b', label='Garis 2')  # Warna biru untuk Garis 2

plt.scatter([x1, x2, x3, x4], [y1, y2, y3, y4], color='red', label='titik')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Dua garis')
plt.legend()
plt.grid()
plt.show()
