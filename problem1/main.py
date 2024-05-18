class BangunDatar:
    def __init__(self, sisi1, sisi2=None):
        self.sisi1 = sisi1
        self.sisi2 = sisi2

    def luas(self):
        pass

    def keliling(self):
        pass


class Persegi(BangunDatar):
    def luas(self):
        return self.sisi1 ** 2

    def keliling(self):
        return 4 * self.sisi1


class Segitiga(BangunDatar):
    def luas(self):
        return int(0.5 * self.sisi1 * self.sisi2)

    def keliling(self):
        return int(self.sisi1 + self.sisi2 + ((self.sisi1 ** 2 + self.sisi2 ** 2) ** 0.5))


class PersegiPanjang(BangunDatar):
    def luas(self):
        return self.sisi1 * self.sisi2

    def keliling(self):
        return 2 * (self.sisi1 + self.sisi2)


def hitung_dan_cetak(bangun_datar):
    luas = bangun_datar.luas()
    keliling = bangun_datar.keliling()
    return luas, keliling


if __name__ == "__main__":
    persegi = Persegi(4)
    segitiga = Segitiga(3, 4)
    persegi_panjang = PersegiPanjang(7, 8)

    print("Luas")
    print("Persegi :", persegi.luas())
    print("Segitiga :", segitiga.luas())
    print("Persegi Panjang :", persegi_panjang.luas())

    print("\nKeliling")
    print("Persegi :", persegi.keliling())
    print("Segitiga :", segitiga.keliling())
    print("Persegi Panjang :", persegi_panjang.keliling())
