# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Un email com a cadena de text.
# Especificacions de sortida:
#   - Mostra l'email si és vàlid, o un missatge d'error si no ho és.
# ================================================================

class CompteUsuari:
    def __init__(self, email):
        self.__email = None  # Inicialitzem __email com a None
        self.email = email  # Utilitzem el setter per validar l'email alhora de crear l'objecte

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if "@" in valor and "." in valor:
            self.__email = valor
        else:
            print("Email no vàlid")

# Exemple d'ús
usuari = CompteUsuari("usuari@domini.com")
print("Email correcte:", usuari.email)

usuari.email = "usuari@domini"  # No té el punt, és invàlid
print("Després de canvi incorrecte:", usuari.email)

usuari.email = "usuari@domini.org"  # Corregit
print("Després de canvi correcte:", usuari.email)
