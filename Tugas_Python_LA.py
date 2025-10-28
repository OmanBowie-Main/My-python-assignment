berat_telur=1 #butuh 5 kilogram
harga_telur=26000 #per 1 kilogram
transport=3500 #sekali naik angkot
uang_ibu=200000 #uang yang ibu bawa

print('ibu memiliki uang sebanyak Rp.', uang_ibu)
print('ibu membutuhkan telur sebanyak', berat_telur*5, 'kg')
print('harga telur per kilogram adalah Rp.', harga_telur)
print('ibu menggunakan ongkos pulang pergi senilai', transport*2)
print('jadi total uang yang ibu butuhkan adalah Rp.', (harga_telur*5)+(transport*2))
print('jadi sisa uang ibu adalah Rp.', uang_ibu-((harga_telur*5)+(transport*2)))