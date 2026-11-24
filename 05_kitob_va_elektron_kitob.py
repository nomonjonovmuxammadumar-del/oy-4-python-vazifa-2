class Kitob:
    def __init__(self, nom: str, muallif: str, sahifa_soni: int):
        self.nom = nom
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def malumot(self):
        return f"Kitob: '{self.nom}', Muallif: {self.muallif}, Sahifalar: {self.sahifa_soni}"


class ElektronKitob(Kitob):
    def __init__(self, nom: str, muallif: str, sahifa_soni: int, format: str, fayl_hajmi: str):
        super().__init__(nom, muallif, sahifa_soni)
        self.format = format
        self.fayl_hajmi = fayl_hajmi

    def malumot(self):
        ota_malumot = super().malumot()
        return f"{ota_malumot}, Format: {self.format}, Hajmi: {self.fayl_hajmi}"


if __name__ == "__main__":
    kitob1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 320)
    kitob2 = ElektronKitob("Python asoslari", "Guido van Rossum", 450, "PDF", "15 MB")

    print(kitob1.malumot())
    print(kitob2.malumot())
