def main():
    # Membuat dua set bilangan bulat
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # Menampilkan set awal
    print("Set 1:", set1)
    print("Set 2:", set2)

    # Operasi pada set
    union_set = set1.union(set2)  # Gabungan dari kedua set
    intersection_set = set1.intersection(set2)  # Irisan dari kedua set
    difference_set1 = set1.difference(set2)  # Perbedaan antara set1 dan set2
    difference_set2 = set2.difference(set1)  # Perbedaan antara set2 dan set1

    # Menampilkan hasil operasi
    print("\nHasil Gabungan:", union_set)
    print("Hasil Irisan:", intersection_set)
    print("Perbedaan Set 1 - Set 2:", difference_set1)
    print("Perbedaan Set 2 - Set 1:", difference_set2)

if __name__ == "__main__":
    main()
