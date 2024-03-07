import numpy as np
import matplotlib.pyplot as plt

# tentukan wilayah
x = np.linspace(-8, 8, 10000)
plt.figure(figsize=(7, 6.5))

# Tentukan persamaan matematika
y1 = (25 - x ** 2) ** 0.5
y2 = -(25 - x ** 2) ** 0.5

y3 = 5 + (4 - (x - 4) ** 2) ** 0.5
y4 = 5 - (4 - (x - 4) ** 2) ** 0.5
y5 = 5 + (4 - (x + 4) ** 2) ** 0.5
y6 = 5 - (4 - (x + 4) ** 2) ** 0.5

# y7 = 1.5 + (2-(x + 2) ** 2) ** 0.5
# y8 = 1.5 - (2-(x + 2) ** 2) ** 0.5
#
# y9 = 1.5 + (2-(x - 2) ** 2) ** 0.5
# y10 = 1.5 - (2-(x - 2) ** 2) ** 0.5

# plt.plot(x,y,'k')
plt.plot(x, y1, '-k')
plt.plot(x, y2, '-k')
plt.plot(x, y3, '-k')
plt.plot(x, y4, '-k')
plt.plot(x, y5, '-k')
plt.plot(x, y6, '-k')
# plt.plot(x, y7, '-k')
# plt.plot(x, y8, '-k')
# plt.plot(x, y9, '-k')
# plt.plot(x, y10, '-k')

# Fill area between curves
plt.fill_between(x, y1, y2, color='black')
plt.fill_between(x, y3, y4, color='black')
plt.fill_between(x, y5, y6, color='black')
# plt.fill_between(x, y7, y8, color='white')
# plt.fill_between(x, y9, y10, color='white')

plt.legend(loc='upper center')
plt.show()
