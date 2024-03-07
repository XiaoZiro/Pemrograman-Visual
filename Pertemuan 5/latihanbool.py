def main():
    # Meminta pengguna untuk memasukkan dua bilangan bulat
    num1 = int(input("Masukkan bilangan bulat pertama: "))
    num2 = int(input("Masukkan bilangan bulat kedua: "))

    # Membandingkan kedua bilangan bulat
    greater_than = num1 > num2
    less_than = num1 < num2
    equal_to = num1 == num2

    # Menampilkan hasil perbandingan dalam bentuk boolean
    print("\nApakah bilangan pertama lebih besar dari bilangan kedua?", greater_than)
    print("Apakah bilangan pertama lebih kecil dari bilangan kedua?", less_than)
    print("Apakah kedua bilangan sama?", equal_to)

if __name__ == "__main__":
    main()
