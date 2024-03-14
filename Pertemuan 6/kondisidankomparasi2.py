# Masukkan posisi piksel pada layar
piksel_row = 300

rowmax = int(1079)
batas1 = int(0.2*rowmax)
batas2 = int(0.4*rowmax)
batas3 = int(0.6*rowmax)
batas4 = int(0.8*rowmax)


print("batas1: ",batas1)
print("batas2: ",batas2)
print("batas3: ",batas3)
print("batas4: ",batas4)
print("rowmax: ", rowmax)

print("Posisi piksel berada pada baris ke-", piksel_row)

if(piksel_row >= 0 and piksel_row < batas1):
    print("warnai piksel merah.")
if(piksel_row >= batas1 and piksel_row < batas2):
    print("warnai piksel hijau.")
if(piksel_row >= batas2 and piksel_row < batas3):
    print("warnai piksel biru.")
if(piksel_row >= batas3 and piksel_row < batas4):
    print("warnai piksel kuning.")
if(piksel_row >= batas4 and piksel_row < rowmax):
    print("warnai piksel ungu.")

