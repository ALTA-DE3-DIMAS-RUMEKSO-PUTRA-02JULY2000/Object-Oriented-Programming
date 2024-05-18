class BangunRuang:
    def __init__(self):
        pass

    def hitung_volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__()
        self.sisi = sisi

    def hitung_volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__()
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        super().__init__()
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def hitung_volume(self):
        return 22 * (self.jari_jari ** 2)//7 * self.tinggi

def hitung_volume_bangun():
    kubus_sisi = 10
    balok_panjang = 3
    balok_lebar = 6
    balok_tinggi = 10
    tabung_jari_jari = 7
    tabung_tinggi = 10

    kubus = Kubus(kubus_sisi)
    balok = Balok(balok_panjang, balok_lebar, balok_tinggi)
    tabung = Tabung(tabung_jari_jari, tabung_tinggi)

    volume_kubus = kubus.hitung_volume()
    volume_balok = balok.hitung_volume()
    volume_tabung = tabung.hitung_volume()

    print("Volume")
    print(f"Kubus : {volume_kubus}")
    print(f"Balok : {volume_balok}")
    print(f"Tabung : {volume_tabung}")

if __name__ == "__main__":
    hitung_volume_bangun()