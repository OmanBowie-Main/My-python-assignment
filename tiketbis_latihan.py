pembeli=input("Input nama pembeli : ")
no_hp=input('Input No. Handphone : ')
jurusan=input("Input jurusan [SBY/BL/LMP] : ")

if jurusan=="SBY":
    namajurusan="Surabaya"
    harga=300000
elif jurusan=="BL" :
    namajurusan="Bali"
    harga=350000
else :
    namajurusan="Lampung"
    harga=500000

jumlah=int(input('Masukkan Jumlah Beli : '))

if jumlah>=3 :
    potongan=(jumlah*harga)*0.1
else :
    potongan=0
total=(jumlah*harga)-potongan
print("--------------------------------".center(50))
print(" PENJUALAN TIKET BUS ".center(50))
print("XYZ".center(50))
print("--------------------------------".center(50))
print("Nama pembeli : "+str(pembeli))
print("No. Handphone : " + str(no_hp))
print("Kode jurusan yang dipilih : " + str(jurusan))
print("Nama kota tujuan : " + str(namajurusan))
print("Harga : ",+(harga) )
print("Jumlah beli : " ,+ (jumlah) )
print("--------------------------------".center(50))
print("Potongan yang didapat : ",+(potongan))
print("Total bayar :",+(total))
ubay=int(input("Masukkan uang bayar : "))
uangkembali=ubay-total
print("Uang kembali : ",+uangkembali)
