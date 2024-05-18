class PengirimanBarang:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_harga(self):
        volume = self.panjang * self.lebar * self.tinggi
        berat_pembulatan = self.berat
        if volume < 50: 
            volume = 50
        if berat_pembulatan % 1 != 0: 
            berat_pembulatan = int(berat_pembulatan) + 1
        harga = berat_pembulatan * 5000
        return harga

panjang = 5
lebar = 2
tinggi = 4
berat = 1

pengiriman = PengirimanBarang(panjang, lebar, tinggi, berat)
harga = pengiriman.hitung_harga()
print("Harga : Rp", harga)
