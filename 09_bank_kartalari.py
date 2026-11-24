class Karta:
    def __init__(self, egasi: str, raqam_oxiri: str, balans: float):
        self.egasi = egasi
        self.raqam_oxiri = raqam_oxiri
        self.balans = balans

    def __str__(self):
        balans_format = f"{self.balans:,.2f}".replace(",", " ")
        return f"Karta egasi: {self.egasi} (**** {self.raqam_oxiri}), Balans: {balans_format} so'm"

    def __gt__(self, other):
        if isinstance(other, Karta):
            return self.balans > other.balans
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Karta):
            return self.balans < other.balans
        return NotImplemented


if __name__ == "__main__":
    karta1 = Karta("Ali Valiyev", "8600", 2500000)
    karta2 = Karta("Vali Aliyev", "9860", 4200000)

    print(karta1)
    print(karta2)

    if karta1 > karta2:
        print(f"{karta1.egasi}ning kartasida ko'proq mablag' mavjud.")
    elif karta1 < karta2:
        print(f"{karta2.egasi}ning kartasida ko'proq mablag' mavjud.")
    else:
        print("Ikkala kartadagi mablag' bir xil.")
