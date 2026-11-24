class FilmKutubxonasi:
    def __init__(self, nom: str, filmlar=None):
        self.nom = nom
        if filmlar is None:
            self.filmlar = []
        else:
            self.filmlar = list(filmlar)

    def film_qoshish(self, film: str):
        self.filmlar.append(film)

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, index):
        return self.filmlar[index]

    def __contains__(self, film):
        return film in self.filmlar


if __name__ == "__main__":
    kutubxona = FilmKutubxonasi("Kino Olami")

    kutubxona.film_qoshish("Interstellar")
    kutubxona.film_qoshish("Inception")
    kutubxona.film_qoshish("Gladiator")

    print(f"Kutubxona nomi: {kutubxona.nom}")
    print(f"Filmlar soni: {len(kutubxona)}")

    print(f"0-indeksdagi film: {kutubxona[0]}")
    print(f"1-indeksdagi film: {kutubxona[1]}")
    print(f"2-indeksdagi film: {kutubxona[2]}")

    print(f"'Interstellar' bormi? -> {'Interstellar' in kutubxona}")
    print(f"'Avatar' bormi? -> {'Avatar' in kutubxona}")
