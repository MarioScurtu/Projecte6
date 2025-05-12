# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Un total de compra (float).
#   - Un objecte d'estratègia de descompte (Descompte20 o similar).
# Especificacions de sortida:
#   - Càlcul del total amb el descompte aplicat.
# ================================================================

class Descompte20:
    def aplicar(self, total):
        return total * 0.2  # 20% de descompte

class DescompteFix:  # Nova classe de descompte
    def aplicar(self, total):
        return 10  # Descompte fix de 10 €

class CarretCompra:
    def __init__(self, total, estrategia_descompte):  # Injecció de dependència
        self.total = total
        self.estrategia_descompte = estrategia_descompte

    def calcular_total_amb_descompte(self):
        descompte = self.estrategia_descompte.aplicar(self.total)
        return self.total - descompte

# Exemple d'ús
descompte_20 = Descompte20()
carret1 = CarretCompra(100, descompte_20)
total_amb_descompte1 = carret1.calcular_total_amb_descompte()
print(f"Total amb descompte 20%: {total_amb_descompte1}")

descompte_fix = DescompteFix()
carret2 = CarretCompra(100, descompte_fix)
total_amb_descompte2 = carret2.calcular_total_amb_descompte()
print(f"Total amb descompte fix: {total_amb_descompte2}")