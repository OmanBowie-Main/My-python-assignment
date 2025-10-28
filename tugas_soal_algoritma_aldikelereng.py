Aldi = int(input("Masukkan jumlah kelereng Aldi: ")) #Input jumlah kelereng Aldi
Budi = Aldi - 15 #hitung jumlah kelereng Budi
#Proses
if Budi < 0:
    print("Masukinnya minimal 15 yaaa:)")
else:
    total_AB = Aldi + Budi
    Anto = 2 * total_AB
    total_AB_Anto = total_AB + Anto
    Agung = total_AB_Anto - 5
    
    #OUTPUT
    print(f"\nHasil perhitungan:")
    print(f"Jumlah kelereng Aldi: {Aldi}")
    print(f"Jumlah kelereng Budi: {Budi}")
    print(f"Jumlah kelereng Anto: {Anto}")
    print(f"Jumlah kelereng Agung: {Agung}")