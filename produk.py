class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama Produk : {self.nama}")
        print(f"Harga Produk : Rp{self.harga}")

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(self, total):
        if total > 5000:
            return total * 0.05
        return 0