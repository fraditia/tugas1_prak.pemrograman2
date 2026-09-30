from produk import Produk

jumlah_produk = int(input("Masukkan jumlah produk: "))

total_seluruh = 0

for i in range(jumlah_produk):
    print(f"\nProduk ke-{i+1}")

    nama_produk = input("Masukkan nama produk: ")
    harga = float(input("Masukkan harga produk: "))
    jumlah_beli = int(input("Masukkan jumlah beli produk: "))

    produk = Produk(nama_produk, harga)

    produk.tampilkan_info()

    total_produk = produk.hitung_total(jumlah_beli)

    print(f"Total pembelian {produk.nama} : Rp{total_produk}")

    total_seluruh += total_produk


diskon = produk.hitung_diskon(total_seluruh)
total_bayar = total_seluruh - diskon

print("\n=== HASIL PEMBELIAN ===")
print(f"Total Pembelian : Rp{total_seluruh}")
print(f"Diskon 5%       : Rp{diskon}")
print(f"Total Bayar     : Rp{total_bayar}")