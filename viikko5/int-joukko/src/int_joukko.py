
class IntJoukko:
    def __init__(self, kapasiteetti=0, kasvatuskoko=0, numero_lista=[]):
        self.lukujono = set(numero_lista)

    def kuuluu(self, numero):
        return numero in self.lukujono

    def lisaa(self, numero):
        if numero in self.lukujono:
            return False
        self.lukujono.add(numero)
        return True

    def poista(self, numero):
        if numero in self.lukujono:
            self.lukujono.remove(numero)
            return True
        return False

    def kopioi_taulukko(self, kopioitava_lista, kohde_lista):
        kohde_lista.clear()
        kohde_lista.extend(kopioitava_lista)

    def mahtavuus(self):
        return len(self.lukujono)

    def to_int_list(self):
        return list(self.lukujono)

    @staticmethod
    def yhdiste(joukko1, joukko2):
        return IntJoukko(numero_lista=joukko1.lukujono.union(joukko2.lukujono))

    @staticmethod
    def leikkaus(joukko1, joukko2):
        return IntJoukko(numero_lista=joukko1.lukujono.intersection(joukko2.lukujono))

    @staticmethod
    def erotus(joukko1, joukko2):
        return IntJoukko(numero_lista=joukko1.lukujono.difference(joukko2.lukujono))

    def __str__(self):
        if len(self.lukujono) > 0:
            return str(self.lukujono)
        else:
            return "{}"
