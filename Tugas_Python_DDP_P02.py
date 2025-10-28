# Print menu makanan
print('=+=+=+=+ Menu Makanan =+=+=+=+')
print('1. Nasi Goreng = Rp. 45000')
print('2. Mie Goreng = Rp. 30000')
print('3. Nasi Timbel = Rp. 55000')

# Print menu minuman
print('\n=+=+=+=+=+ Menu Minuman =+=+=+=+=+')
print('1. Es Teh = Rp. 5000')
print('2. Es Jeruk = Rp. 10000')

# Input nama
print('\nSilahkan isi nama pemesanan anda')
nama = input('Masukkan Nama: ')

# Input makanan
print('Silahkan pilih menu makanan')
makanan = input('Pilihan Makanan (1/2/3): ')
if makanan == '1':
    harga_makanan = 45000
    makanan_pesan = 'Nasi Goreng'
elif makanan == '2':
    harga_makanan = 30000
    makanan_pesan = 'Mie Goreng'
elif makanan == '3':
    harga_makanan = 55000
    makanan_pesan = 'Nasi Timbel'
else:
    harga_makanan = 0
    makanan_pesan = 'Tidak ada pesanan makanan'

# Input minuman
print('Silahkan pilih menu minuman')
minuman = input('Pilihan Minuman (1/2): ')
if minuman == '1':
    harga_minuman = 5000
    minuman_pesan = 'Es Teh'
elif minuman == '2':
    harga_minuman = 10000
    minuman_pesan = 'Es Jeruk'
else:
    harga_minuman = 0
    minuman_pesan = 'Tidak ada pesanan minuman'

# Hitung total
total_harga = harga_makanan + harga_minuman
print('\nTotal harga yang harus dibayar adalah Rp.' + str(total_harga))

# Input uang dibayar
print('Masukkan uang yang dibawa untuk bayar:')
bayar = int(input('Jumlah (Rp.): '))
kembalian = bayar - total_harga

# Print struk
print('\n=+=+=+=+ Struk Pembayaran =+=+=+=+')
print('Nama Pemesan: ' + nama)
print('Pesanan Makanan: ' + makanan_pesan + ' = Rp.' + str(harga_makanan))
print('Pesanan Minuman: ' + minuman_pesan + ' = Rp.' + str(harga_minuman))
print('Total Harga: Rp.' + str(total_harga))
print('Uang Dibayar: Rp.' + str(bayar))
print('Kembalian: Rp.' + str(kembalian))
print('Terima kasih sudah berkunjung!')