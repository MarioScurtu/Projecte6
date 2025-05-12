# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Un objecte de tipus Animal (o subclasse).
# Especificacions de sortida:
#   - Retorn del so de l'animal ("Miau", "Muuu").
#   - Impressió del so de l'animal.
# ================================================================

class Animal:
    def fer_soroll(self):
        pass

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

def reproduir_soroll(animal):
    print(animal.fer_soroll())

# Exemple d'ús
gat = Gat()
vaca = Vaca()

reproduir_soroll(gat)
reproduir_soroll(vaca)