# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Coordenades de dos punts.
# Especificacions de sortida:
#   - Mostra la distància entre ells.
# ================================================================

import math
class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre):
        return math.sqrt((self.x - altre.x)**2 + (self.y - altre.y)**2)

# Exemple
p1 = Punt(0, 0)
p2 = Punt(3, 4)
print("Distància:", p1.distancia(p2))
