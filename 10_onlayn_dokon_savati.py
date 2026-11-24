class Mahsulot:
    def __init__(self, nom: str, narx: float):
        self.nom = nom
        self.narx = narx

    def __str__(self):
        return f"{self.nom} ({self.narx:,} so'm)"


class Savat:
    def __init__(self, nomi: str = "Asosiy savat", mahsulotlar=None):
        self.nomi = nomi
        if mahsulotlar is None:
            self.mahsulotlar = []
        else:
            self.mahsulotlar = list(mahsulotlar)

    def qoshish(self, mahsulot: Mahsulot):
        self.mahsulotlar.append(mahsulot)

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        return sum(m.narx for m in self.mahsulotlar)

    def __str__(self):
        return f"Savat: '{self.nomi}', Mahsulotlar soni: {len(self.mahsulotlar)} ta"


if __name__ == "__main__":
    bosh_savat = Savat("Bo'sh savatcha")
    print(bosh_savat)
    if bosh_savat:
        print("Savatda mahsulotlar bor.")
    else:
        print("Savat hozircha bo'sh.\n")

    mening_savatim = Savat("Mening xaridlarim")

    olma = Mahsulot("Olma (1 kg)", 15000)
    non = Mahsulot("Non", 4000)
    sut = Mahsulot("Sut (1 litr)", 12000)
    shokolad = Mahsulot("Shokolad", 25000)

    mening_savatim.qoshish(olma)
    mening_savatim.qoshish(non)
    mening_savatim.qoshish(sut)
    mening_savatim.qoshish(shokolad)

    print(mening_savatim)
    print(f"Savatdagi mahsulotlar soni: {len(mening_savatim)} ta")

    if mening_savatim:
        narx_format = f"{mening_savatim.umumiy_narx():,}".replace(",", " ")
        print(f"Savat bo'sh emas. Umumiy narx: {narx_format} so'm")
    else:
        print("Savat bo'sh!")
