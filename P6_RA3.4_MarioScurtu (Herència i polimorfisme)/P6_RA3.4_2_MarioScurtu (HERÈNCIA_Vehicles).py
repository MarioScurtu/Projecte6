# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Marca del vehicle (string).
# Especificacions de sortida:
#   - Impressió del missatge d'arrencada.
#   - Impressió del so del clàxon ("Pip pip!").
# ================================================================

class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"El vehicle {self.marca} està arrencant.")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")

# Exemple d'ús
cotxe = Cotxe("Seat")
cotxe.arrencar()
cotxe.tocar_claxon()