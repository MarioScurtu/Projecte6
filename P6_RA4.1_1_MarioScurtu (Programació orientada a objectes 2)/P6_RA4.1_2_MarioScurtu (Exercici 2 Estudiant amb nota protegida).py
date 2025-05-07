# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Nota entre 0 i 10.
# Especificacions de sortida:
#   - Mostra la nota o missatge si no és vàlida.
# ================================================================

class Estudiant:
    def __init__(self, nota):
        self._nota = 0
        self.modificar_nota(nota)

    def llegir_nota(self):
        return self._nota

    def modificar_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota

# Exemple d'ús
alumne = Estudiant(8)
print("Nota:", alumne.llegir_nota())
alumne.modificar_nota(11)
print("Nota després de modificar:", alumne.llegir_nota())
