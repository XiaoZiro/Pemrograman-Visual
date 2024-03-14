
a = float(input("Masukkan nilai a ="))
b = float(input("Masukkan nilai b ="))

print("\nnilai a = ",a)
print("nilai b =",b)

a_besar = a>b
print("\nApakah a lebih besar dari b ?", a_besar)

b_besar = b>a
print("Apakah b lebih besar dari a ?", b_besar)

sama = a==b
print("Apakah a sama dengan b ?", sama)

if a > 10000:
    ppn_a = a * 0.12
else:
    ppn_a = 0
print("Nilai ppn a lebih besar dari 10000 adalah ", ppn_a)

if b > 50000:
    ppn_b = b * 0.12
else:
    ppn_b = 0
print("Nilai ppn b lebih besar dari 50000 adalah ", ppn_b)

total_ppn = ppn_a + ppn_b
print("\ntotal ppn yaitu ", total_ppn)

del a,b
a_hapus = 'a' not in locals()
b_hapus = 'b' not in locals()

print("Apakah a telah dihapus? ", a_hapus)
print("Apakah b telah dihapus? ", b_hapus)