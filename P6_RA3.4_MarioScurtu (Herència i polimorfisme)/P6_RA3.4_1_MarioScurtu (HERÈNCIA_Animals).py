# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Cap entrada.
# Especificacions de sortida:
#   - Impressió del so que fa cada animal ("Bup bup!", "Miau!").
# ================================================================

class Animal:
    def parlar(self):
        pass  # Mètode buit a la classe base

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")

# Exemple d'ús
gos = Gos()
gat = Gat()

gos.parlar()
gat.parlar()