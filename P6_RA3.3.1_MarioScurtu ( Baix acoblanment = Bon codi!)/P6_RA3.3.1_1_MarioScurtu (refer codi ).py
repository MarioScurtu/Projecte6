# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Un client (string).
#   - Un import total (float).
#   - Un objecte impressora (ImpressoraPDF o similar).
# Especificacions de sortida:
#   - Impressió de la factura a través de l'objecte impressora.
# ================================================================

class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")

class ImpressoraHTML:  # Nova classe d'impressora
    def imprimir(self, contingut):
        print(f"Imprimint HTML: {contingut}")

class Factura:
    def __init__(self, client, import_total, impressora):  # Injecció de dependència
        self.client = client
        self.import_total = import_total
        self.impressora = impressora

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)

# Exemple d'ús
impressora_pdf = ImpressoraPDF()
factura1 = Factura("Joan", 100, impressora_pdf)
factura1.imprimir_factura()

impressora_html = ImpressoraHTML()
factura2 = Factura("Maria", 200, impressora_html)
factura2.imprimir_factura()