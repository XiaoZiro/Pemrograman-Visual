# Masukkan posisi piksel pada layar
piksel_row = 100

rowmax = int(1079)
batas1 = int(0.5*rowmax)

print("batas1: ",batas1)
print("Posisi piksel berada pada baris ke-", piksel_row)

if piksel_row < batas1:
    print("warnai piksel merah.")
if piksel_row == batas1:
    print("Warnai piksel hitam.")
if piksel_row > batas1:
    print("warnai piksel putih.")
if piksel_row <= batas1:
    print("warnai piksel kuning.")
if piksel_row >= batas1:
    print("warnai piksel unggu.")