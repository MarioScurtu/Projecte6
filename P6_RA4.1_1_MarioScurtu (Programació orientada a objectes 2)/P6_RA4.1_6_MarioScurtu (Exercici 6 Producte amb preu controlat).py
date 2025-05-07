# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Preu > 0
# Especificacions de sortida:
#   - Mostra el preu o error si és invàlid.
# ================================================================

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu

    @property
    def preu(self):
        return self.__preu

    @preu.setter
    def preu(self, valor):
        if valor > 0:
            self.__preu = valor
        else:
            print("Preu no vàlid")

# Exemple d'ús
producte = Producte("Llaptop", 500)
print("Preu:", producte.preu)
producte.preu = -100  # Error
