def hanoi(n, asal, bantu, tujuan):
    if n == 1:
        print(f"Piringan 1 dari {asal} → {tujuan}")
    else:
        hanoi(n-1, asal, tujuan, bantu)
        print(f"Piringan {n} dari {asal} → {tujuan}")
        hanoi(n-1, bantu, asal, tujuan)

print("PROGRAM MENARA HANOI")
print("=" * 30)

n = int(input("Masukkan jumlah piringan: "))

print(f"\nLangkah memindahkan {n} piringan:")
hanoi(n, 'A', 'B', 'C')
print(f"\nSelesai! Total langkah: {2**n - 1}")