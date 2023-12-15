
class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, other):
        numarator_nou = self.numarator * other.numitor + other.numarator * self.numitor
        numitor_nou = self.numitor * other.numitor
        return Fractie(numarator_nou, numitor_nou)

    def __sub__(self, other):
        numarator_nou = self.numarator * other.numitor - other.numarator * self.numitor
        numitor_nou = self.numitor * other.numitor
        return Fractie(numarator_nou, numitor_nou)

    def inverse(self):
        if self.numarator != 0:
            return Fractie(self.numitor, self.numarator)


fractie1 = Fractie(1, 2)
fractie2 = Fractie(1,3)

suma = fractie1 + fractie2
diferenta = fractie1 - fractie2
inversa_fractiei = fractie1.inverse()

print(f"Fractia 1: {fractie1}")
print(f"Fractia 2: {fractie2}")
print(f"Suma: {suma}")
print(f"Diferenta: {diferenta}")
print(f"Inversa fractiei 1: {inversa_fractiei}")

