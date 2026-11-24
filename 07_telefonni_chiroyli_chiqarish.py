class Telefon:
    def __init__(self, brend: str, model: str, narx: int):
        self.brend = brend
        self.model = model
        self.narx = narx

    def __str__(self):
        narx_format = f"{self.narx:,}".replace(",", " ")
        return f"{self.brend} {self.model} — {narx_format} so'm"

    def __eq__(self, other):
        if isinstance(other, Telefon):
            return self.narx == other.narx
        return False


if __name__ == "__main__":
    telefon1 = Telefon("Samsung", "A54", 4500000)
    telefon2 = Telefon("Xiaomi", "Redmi Note 13 Pro", 4500000)
    telefon3 = Telefon("Apple", "iPhone 15 Pro", 14500000)

    print(telefon1)
    print(telefon2)
    print(telefon3)

    print(f"'{telefon1.model}' va '{telefon2.model}' narxi tengmi? -> {telefon1 == telefon2}")
    print(f"'{telefon1.model}' va '{telefon3.model}' narxi tengmi? -> {telefon1 == telefon3}")
