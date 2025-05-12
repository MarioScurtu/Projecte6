# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Una llista d'objectes de tipus Vehicle (o subclasses).
# Especificacions de sortida:
#   - Simulació del moviment de cada vehicle.
# ================================================================

class Vehicle:
    def moure(self):
        pass

class Cotxe(Vehicle):
    def moure(self):
        print("El cotxe està conduint per la carretera.")

class Bicicleta(Vehicle):
    def moure(self):
        print("La bicicleta està pedalant pel carril bici.")

class Barca(Vehicle):
    def moure(self):
        print("La barca està navegant pel riu.")

def simular_moviment(vehicles):
    for vehicle in vehicles:
        vehicle.moure()

# Exemple d'ús
vehicles = [Cotxe(), Bicicleta(), Barca()]

simular_moviment(vehicles)