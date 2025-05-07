# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Amplada i alçada d’un rectangle.
# Especificacions de sortida:
#   - Mostra l’àrea i el perímetre del rectangle.
# ================================================================

class Rectangle:
    def __init__(self, amplada, alcada):
        self.amplada = amplada
        self.alcada = alcada

    def area(self):
        return self.amplada * self.alcada

    def perimetre(self):
        return 2 * (self.amplada + self.alcada)

# Exemple
r = Rectangle(4, 3)
print("Àrea:", r.area())
print("Perímetre:", r.perimetre())
