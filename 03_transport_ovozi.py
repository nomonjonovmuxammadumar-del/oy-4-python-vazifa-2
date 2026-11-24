class Transport:
    def __init__(self, nomi: str):
        self.nomi = nomi

    def harakatlanish(self):
        print(f"{self.nomi} harakatlanmoqda.")


class Mashina(Transport):
    def __init__(self, nomi: str = "Mashina"):
        super().__init__(nomi)

    def harakatlanish(self):
        print(f"{self.nomi}: Yo'lda motor shovqini bilan ketmoqda (Vrum-vrum!).")


class Velosiped(Transport):
    def __init__(self, nomi: str = "Velosiped"):
        super().__init__(nomi)

    def harakatlanish(self):
        print(f"{self.nomi}: Pedallarni aylantirib jimgina ketmoqda (Jiring-jiring!).")


class Poyezd(Transport):
    def __init__(self, nomi: str = "Poyezd"):
        super().__init__(nomi)

    def harakatlanish(self):
        print(f"{self.nomi}: Temir yo'lda gupurlab ketmoqda (Chux-chux!).")


if __name__ == "__main__":
    mashina = Mashina("Malibu")
    velosiped = Velosiped("Trek")
    poyezd = Poyezd("Afrosiyob")

    transportlar = [mashina, velosiped, poyezd]

    for transport in transportlar:
        transport.harakatlanish()
