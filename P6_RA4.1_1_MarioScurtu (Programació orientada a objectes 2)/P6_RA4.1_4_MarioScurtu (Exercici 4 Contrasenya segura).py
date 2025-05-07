# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Contrasenya amb mínim 8 caràcters.
# Especificacions de sortida:
#   - Canvia la contrasenya o mostra error.
# ================================================================

class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya

    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya
        else:
            print("La contrasenya ha de tenir almenys 8 caràcters.")

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau

# Exemple d'ús
usuari = Usuari("abc12345")
usuari.canviar_contrasenya("1234")  # Error
usuari.canviar_contrasenya("nova12345")
print("Contrasenya verificada:", usuari.verificar_contrasenya("nova12345"))
