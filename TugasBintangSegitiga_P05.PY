def main():
    while True:
        try:
            height = int(input("Masukkan tinggi segitiga (5-10): "))
            if 5 <= height <= 10:
                break
            else:
                print("Tinggi harus antara 5 dan 10. Coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")

    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == "__main__":
    main()