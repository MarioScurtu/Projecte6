# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Cap, només interacció amb mètodes.
# Especificacions de sortida:
#   - Mostra la puntuació actual o la reinicia.
# ================================================================

class Joc:
    def __init__(self):
        self.__puntuacio = 0

    def sumar_punts(self, punts):
        self.__puntuacio += punts

    def reiniciar(self):
        self.__puntuacio = 0

    @property
    def puntuacio(self):
        return self.__puntuacio

# Exemple d'ús
joc = Joc()
joc.sumar_punts(10)
print("Puntuació:", joc.puntuacio)
joc.reiniciar()
print("Puntuació després de reiniciar:", joc.puntuacio)
