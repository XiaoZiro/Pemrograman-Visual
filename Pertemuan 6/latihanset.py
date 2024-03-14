makanan_1 = {"nasi goreng","mie goreng", "kwetiau goreng","kentang sambel","tempe goreng"}
makanan_2 = {"mie ayam","bakso","bakwan"}

print("\n       Warung Makan Pak Iqbal      ")
print("\n===== Print ======")
print("makanan dalam menu=",makanan_1)

print("\n===== Add ======")
makanan_sebelum = makanan_1.copy()
makanan_1.add("cah kangkung")
tambah_makanan = makanan_1 - makanan_sebelum
print("makanan yang ditambahkan yaitu ", tambah_makanan)
print("makanan dalam menu sekarang yaitu", makanan_1)

print("\n===== Remove =====")
makanan_sebelum_hapus = makanan_1.copy()
makanan_1.remove("kentang sambel")
hapus_makanan = makanan_sebelum_hapus - makanan_1
print("makanan tidak jadi ditambahkan yaitu menu", hapus_makanan)
print("makanan dalam menu Warung Makan Pak Iqbal sekarang yaitu", makanan_1)

print("\n===== Pop ======")
print("Pak Iqbal merasa bahwa makanan yang ada di menu terlalu banyak, maka dari itu Pak Iqbal ingin menghapus menu makanannya")
menu_sebelum = makanan_1.copy()
makanan_1.pop()
menu_makanandihapus = makanan_sebelum - makanan_1
print("makanan yang dihilangkan dalam menu agar tidak mempersulit pak Iqbal yaitu", menu_makanandihapus)

print("\n===== Clear =====")
makanan_1.clear()
print("Warung Pak Iqbal tidak menjual makanan lagi ", makanan_1)

print("\n===== ")