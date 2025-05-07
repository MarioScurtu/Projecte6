# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Hores entre 0 i 23.
# Especificacions de sortida:
#   - Mostra l'hora en format “HH:00” o error si no és vàlida.
# ================================================================

class Rellotge:
    def __init__(self):
        self.__hores = 0

    @property
    def hores(self):
        return self.__hores

    @hores.setter
    def hores(self, hora):
        if 0 <= hora <= 23:
            self.__hores = hora
        else:
            print("Hora no vàlida")

    def mostrar_hores(self):
        return f"{self.__hores}:00"

# Exemple d'ús
rellotge = Rellotge()
rellotge.hores = 15
print("Hora:", rellotge.mostrar_hores())
rellotge.hores = 25  # Error
