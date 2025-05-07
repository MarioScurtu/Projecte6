# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Cap, només interacció amb mètodes.
# Especificacions de sortida:
#   - Mostra el saldo o errors si escau.
# ================================================================

class CompteBancari:
    def __init__(self):
        self.__saldo = 0

    def ingressar(self, quantitat):
        self.__saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.__saldo:
            self.__saldo -= quantitat

    def consultar_saldo(self):
        return self.__saldo

# Exemple d'ús
compte = CompteBancari()
compte.ingressar(100)
compte.retirar(30)
print("Saldo:", compte.consultar_saldo())

