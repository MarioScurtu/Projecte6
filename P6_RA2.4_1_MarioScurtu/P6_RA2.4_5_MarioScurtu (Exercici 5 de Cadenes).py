# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Substitueix totes les lletres "a" per "@" en una frase.
#
# Especificacions d'entrada:
#   - L'usuari ha d'escriure una frase.
# ================================================================

frase = input("Escriu una frase: ")
nova_frase = frase.replace("a", "@").replace("A", "@")
print("Frase modificada:", nova_frase)

