# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Costat del quadrat (float).
#   - Radi del cercle (float).
# Especificacions de sortida:
#   - Impressió de l'àrea de cada figura.
# ================================================================

import math

class Figura:
    def area(self):
        print("Àrea no definida")

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat * self.costat

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * self.radi ** 2

# Exemple d'ús
quadrat = Quadrat(5)
cercle = Cercle(3)

print(f"Àrea del quadrat: {quadrat.area()}")
print(f"Àrea del cercle: {cercle.area()}")