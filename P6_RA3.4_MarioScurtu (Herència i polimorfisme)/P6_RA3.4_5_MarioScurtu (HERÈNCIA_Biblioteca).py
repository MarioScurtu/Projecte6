# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Títol del llibre (string).
#   - Autor del llibre (string).
#   - Nombre de pàgines (enter) per LlibrePaper.
#   - Format (string) per LlibreDigital.
# Especificacions de sortida:
#   - Impressió de la informació específica de cada tipus de llibre.
# ================================================================

class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines

    def mostrar_info(self):
        super().mostrar_info()
        print(f", Nombre de pàgines: {self.n_pagines}")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        super().mostrar_info()
        print(f", Format: {self.format}")

# Exemple d'ús
llibre_paper = LlibrePaper("El Senyor dels Anells", "J.R.R. Tolkien", 1000)
llibre_digital = LlibreDigital("1984", "George Orwell", "ePub")

llibre_paper.mostrar_info()
llibre_digital.mostrar_info()