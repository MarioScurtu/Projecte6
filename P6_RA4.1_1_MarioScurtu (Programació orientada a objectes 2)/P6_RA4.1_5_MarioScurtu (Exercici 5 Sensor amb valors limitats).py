# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Valor entre 0 i 100.
# Especificacions de sortida:
#   - Mostra el valor actual o error si està fora de rang.
# ================================================================

class Sensor:
    def __init__(self):
        self.__valor = 0

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if 0 <= valor <= 100:
            self.__valor = valor
        else:
            print("Valor no vàlid")

# Exemple d'ús
sensor = Sensor()
sensor.valor = 50
print("Valor del sensor:", sensor.valor)
sensor.valor = 120  # Error
