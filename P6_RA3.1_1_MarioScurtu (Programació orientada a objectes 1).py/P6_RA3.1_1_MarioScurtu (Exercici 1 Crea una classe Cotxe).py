# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Marca, model i any del cotxe.
# Especificacions de sortida:
#   - Mostra la informació del cotxe.
# ================================================================

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Model:", self.model)
        print("Any:", self.any)

# Exemple d'ús
cotxe1 = Cotxe("Toyota", "Corolla", 2020)
cotxe1.mostrar_info()
