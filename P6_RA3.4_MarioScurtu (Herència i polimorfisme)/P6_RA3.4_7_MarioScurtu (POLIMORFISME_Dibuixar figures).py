# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Una llista d'objectes de tipus Figura (o subclasses).
# Especificacions de sortida:
#   - Impressió d'una representació de cada figura.
# ================================================================

class Figura:
    def dibuixar(self):
        pass

class Cercle(Figura):
    def dibuixar(self):
        print("Dibuixant un cercle")

class Quadrat(Figura):
    def dibuixar(self):
        print("Dibuixant un quadrat")

class Triangle(Figura):
    def dibuixar(self):
        print("Dibuixant un triangle")

# Exemple d'ús
figures = [Cercle(), Quadrat(), Triangle()]

for figura in figures:
    figura.dibuixar()