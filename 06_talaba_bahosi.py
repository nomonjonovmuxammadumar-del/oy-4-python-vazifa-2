class Inson:
    def __init__(self, ism: str, yosh: int):
        self.ism = ism
        self.yosh = yosh


class Talaba(Inson):
    def __init__(self, ism: str, yosh: int, universitet: str, baho: float):
        super().__init__(ism, yosh)
        self.universitet = universitet
        self.baho = baho

    def natija(self):
        if 86 <= self.baho <= 100:
            return "A'lo"
        elif 71 <= self.baho <= 85:
            return "Yaxshi"
        elif 56 <= self.baho <= 70:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"


if __name__ == "__main__":
    talaba1 = Talaba("Sanjar", 20, "TATU", 92)
    talaba2 = Talaba("Dilshod", 21, "O'zMU", 75)
    talaba3 = Talaba("Jasur", 19, "TDTU", 62)
    talaba4 = Talaba("Alisher", 22, "SamDU", 48)

    for talaba in [talaba1, talaba2, talaba3, talaba4]:
        print(f"Talaba: {talaba.ism}, Baho: {talaba.baho} -> Natija: {talaba.natija()}")
