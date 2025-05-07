# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Nom i nota de l’estudiant.
# Especificacions de sortida:
#   - Indicar si ha aprovat o no.
# ================================================================

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        return self.nota >= 5

# Exemple
e = Estudiant("Joan", 6)
print(f"{e.nom} ha aprovat:", e.ha_aprovat())
