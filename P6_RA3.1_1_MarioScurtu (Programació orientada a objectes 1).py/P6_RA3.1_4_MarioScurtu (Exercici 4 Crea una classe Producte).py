# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Nom i preu del producte.
# Especificacions de sortida:
#   - Preu amb el descompte aplicat.
# ================================================================

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def aplicar_descompte(self, percentatge):
        self.preu -= self.preu * (percentatge / 100)

# Exemple
p = Producte("Ordinador", 1000)
p.aplicar_descompte(10)
print("Preu amb descompte:", p.preu)
