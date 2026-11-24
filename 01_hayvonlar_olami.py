class Hayvon:
    def __init__(self, nomi: str, yoshi: int):
        self.nomi = nomi
        self.yoshi = yoshi

    def ovoz(self):
        print(f"{self.nomi} ovoz chiqarmoqda.")


class It(Hayvon):
    def __init__(self, nomi: str, yoshi: int):
        super().__init__(nomi, yoshi)

    def qoriqlash(self):
        print(f"{self.nomi} uyni qo'riqlamoqda.")


class Mushuk(Hayvon):
    def __init__(self, nomi: str, yoshi: int):
        super().__init__(nomi, yoshi)

    def sichqon_tutish(self):
        print(f"{self.nomi} sichqon tutmoqda.")


if __name__ == "__main__":
    it = It("Olapar", 3)
    mushuk = Mushuk("Mosh", 2)

    it.ovoz()
    mushuk.ovoz()

    it.qoriqlash()
    mushuk.sichqon_tutish()
