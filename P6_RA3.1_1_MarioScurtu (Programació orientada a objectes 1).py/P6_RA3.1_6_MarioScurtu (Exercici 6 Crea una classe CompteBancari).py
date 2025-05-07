# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Operacions de saldo: ingrés i retirada.
# Especificacions de sortida:
#   - Mostra el saldo actual.
# ================================================================

class CompteBancari:
    def __init__(self):
        self.saldo = 0

    def ingressar(self, quantitat):
        self.saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
        else:
            print("Saldo insuficient.")

    def veure_saldo(self):
        print("Saldo actual:", self.saldo)

# Exemple
c = CompteBancari()
c.ingressar(100)
c.retirar(30)
c.veure_saldo()
