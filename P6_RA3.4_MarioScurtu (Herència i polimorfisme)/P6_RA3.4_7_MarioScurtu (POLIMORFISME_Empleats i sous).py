# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Una llista d'objectes de tipus Empleat (o subclasses).
# Especificacions de sortida:
#   - Impressió del sou de cada empleat.
# ================================================================

class Empleat:
    def __init__(self, nom):
        self.nom = nom

    def calcular_sou(self):
        pass

class Fixe(Empleat):
    def __init__(self, nom, sou_mensual):
        super().__init__(nom)
        self.sou_mensual = sou_mensual

    def calcular_sou(self):
        return self.sou_mensual

class Autonom(Empleat):
    def __init__(self, nom, hores_treballades, tarifa_hora):
        super().__init__(nom)
        self.hores_treballades = hores_treballades
        self.tarifa_hora = tarifa_hora

    def calcular_sou(self):
        return self.hores_treballades * self.tarifa_hora

def mostrar_sous(llista_empleats):
    for empleat in llista_empleats:
        print(f"Sou de {empleat.nom}: {empleat.calcular_sou()}")

# Exemple d'ús
empleats = [
    Fixe("Joan", 2000),
    Autonom("Maria", 40, 25),
    Fixe("Pere", 2500)
]

mostrar_sous(empleats)