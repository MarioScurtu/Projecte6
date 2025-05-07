# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Temperatura entre 10 i 30°C.
# Especificacions de sortida:
#   - Mostra la temperatura configurada o error si no és vàlida.
# ================================================================

class Termostat:
    def __init__(self):
        self.__temperatura = 20  # Temperatura per defecte

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 10 <= valor <= 30:
            self.__temperatura = valor
        else:
            print("Temperatura no vàlida")

# Exemple d'ús
termostat = Termostat()
termostat.temperatura = 25
print("Temperatura:", termostat.temperatura)
termostat.temperatura = 35  # Temperatura no vàlida
