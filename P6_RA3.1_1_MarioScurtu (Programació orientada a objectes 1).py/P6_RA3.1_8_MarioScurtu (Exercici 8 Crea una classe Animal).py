# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Nom i espècie de l’animal.
# Especificacions de sortida:
#   - Missatge genèric de soroll.
# ================================================================

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print("Fa un soroll")

# Exemple
a = Animal("Tigre", "Felí")
a.fer_soroll()
