# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Radi del cercle.
# Especificacions de sortida:
#   - Mostra l’àrea i el perímetre del cercle.
# ================================================================

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * self.radi ** 2

    def perimetre(self):
        return 2 * math.pi * self.radi

# Exemple
c = Cercle(5)
print("Àrea:", c.area())
print("Perímetre:", c.perimetre())
