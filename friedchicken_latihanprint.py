print("GEROBAK FRIED CHICKEN".center (50))
print("-" * 40 )
print("Kode | Jenis Potong  |Harga")
print("D    | Dada          |Rp. 25000")
print("P    | Paha          |Rp. 20000")
print("S    | Sayap         |Rp. 15000")
print("-" * 40 )

banyak_jenis = int(input("Banyak Jenis : "))

menu = {
    'D': {'nama': 'Dada', 'harga': 25000},
    'P': {'nama': 'Paha', 'harga': 20000},
    'S': {'nama': 'Sayap', 'harga': 15000}
}

pesanan = []

for i in range(banyak_jenis):
    print(f"Jenis Ke - {i+1}")
    kode = input("Kode Potong [D/P/S] : ").upper()
    
    while kode not in menu:
        print("Kode gak valid bro! Masukkin D, P, atau S")
        kode = input("Kode Potong [D/P/S] : ").upper()
    
    banyak_potong = int(input("Banyak Potong : "))
    
    harga_satuan = menu[kode]['harga']
    jumlah_harga = harga_satuan * banyak_potong
    
    pesanan.append({
        'nama': menu[kode]['nama'],
        'harga_satuan': harga_satuan,
        'banyak_beli': banyak_potong,
        'jumlah_harga': jumlah_harga
    })

print("\n" + "=" * 50)
print("GEROBAK FRIED CHICKEN")
print("-" * 50)
print("No. Jenis     Harga    Banyak    Jumlah")
print("    Potong    Satuan    Beli     Harga")
print("-" * 50)

total_bayar = 0
for i, item in enumerate(pesanan, 1):
    print(f"{i:2}. {item['nama']:6}   Rp {item['harga_satuan']:4}   {item['banyak_beli']:6}   Rp {item['jumlah_harga']:6}")
    total_bayar += item['jumlah_harga']

print("-" * 50)

pajak = total_bayar * 0.10
total_setelah_pajak = total_bayar + pajak

print(f"Jumlah Bayar Rp {total_bayar:6}")
print(f"Pajak 10%    Rp {pajak:6.0f}")
print(f"Total Bayar  Rp {total_setelah_pajak:6.0f}")