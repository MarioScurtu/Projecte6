# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Edat no negativa.
# Especificacions de sortida:
#   - Mostra l’edat o error si és negativa.
# ================================================================

class Alumne:
    def __init__(self):
        self.__edat = 0

    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, edat):
        if edat >= 0:
            self.__edat = edat
        else:
            print("Edat no vàlida")

# Exemple d'ús
alumne = Alumne()
alumne.edat = 18
print("Edat:", alumne.edat)
alumne.edat = -5  # Error
