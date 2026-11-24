class Shakl:
    def __init__(self, nomi: str):
        self.nomi = nomi

    def yuza(self):
        return 0


class Kvadrat(Shakl):
    def __init__(self, tomon: float):
        super().__init__("Kvadrat")
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2


class TogriTortburchak(Shakl):
    def __init__(self, boyi: float, eni: float):
        super().__init__("To'g'ri to'rtburchak")
        self.boyi = boyi
        self.eni = eni

    def yuza(self):
        return self.boyi * self.eni


if __name__ == "__main__":
    shakllar = [
        Kvadrat(5),
        TogriTortburchak(6, 4),
        Kvadrat(8),
        TogriTortburchak(10, 3)
    ]

    for shakl in shakllar:
        print(f"{shakl.nomi} yuzasi: {shakl.yuza()}")
