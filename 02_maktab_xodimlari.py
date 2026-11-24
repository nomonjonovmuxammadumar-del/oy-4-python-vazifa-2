class Xodim:
    def __init__(self, ism: str, maosh: float):
        self.ism = ism
        self.maosh = maosh

    def malumot(self):
        return f"Xodim: {self.ism}, Maoshi: {self.maosh:,} so'm"


class Oqituvchi(Xodim):
    def __init__(self, ism: str, maosh: float, fan: str):
        super().__init__(ism, maosh)
        self.fan = fan

    def malumot(self):
        ota_malumot = super().malumot()
        return f"{ota_malumot}, Fani: {self.fan}"


class Farrosh(Xodim):
    def __init__(self, ism: str, maosh: float, qavat: int):
        super().__init__(ism, maosh)
        self.qavat = qavat

    def malumot(self):
        ota_malumot = super().malumot()
        return f"{ota_malumot}, Qavati: {self.qavat}-qavat"


if __name__ == "__main__":
    oqituvchi = Oqituvchi("Akmal Berdiyev", 5000000, "Matematika")
    farrosh = Farrosh("Zulfiya Rahimova", 2800000, 3)

    print(oqituvchi.malumot())
    print(farrosh.malumot())
