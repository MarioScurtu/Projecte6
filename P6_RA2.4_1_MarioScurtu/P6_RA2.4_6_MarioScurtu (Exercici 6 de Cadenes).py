# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Mostra la primera i l'última lletra d'una cadena.
#
# Especificacions d'entrada:
#   - L'usuari ha d'escriure una cadena de text.
# ================================================================

text = input("Escriu una cadena: ")

if len(text) > 0:
    print("Primera lletra:", text[0])
    print("Última lletra:", text[-1])
else:
    print("La cadena està buida.")
