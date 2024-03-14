print("Case 1")

# data tipe boolean
f = bool(True)
g = bool(False)
print(f)
print(g)
print("=====================================================")

# case 2
print("Case 2")

# data bertipe boolean dalam berbagai konteks
print(3>2)
print(3+2 == 5)
print(3<2)
print("======================================================")

# case 3
print("case 3")

# data bertipe boolean dalam berbagai konteks
Penghasilan = 200000000
PenghasilanTanpaPajak = 4000000

if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0.1 * Penghasilan
print("Pajak yang harus anda bayar: Rp ", PajakYangHarusDibayar)

#Part 2
# Case 4

print("case 4")
# semua data yang tidak nol
a =3
b = "Ini data string"
c = ("laptop", "buku","ballpen")
d = ["laptop", "buku","ballpen"]
e = {"laptop":"asus", "buku":"buku_teks","ballpen":"arrow"}
f = {1,2,3,4,5}

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("================================================")


# Part 3
# Case 5

print("Case 5")

# variabel yang kosong memiliki nilai boolean false
a = 0
b = ""
c = ()
d = []
e = {}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("=========================================")

#CASE 6
print("Case 6")
# variabel yang panjangnya nol memiliki nilai boolean false
class myclass():
    def __len__(self):
        return 0
print(bool(myclass()))
print("=======================================================")