# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Comprova si una paraula és un palíndrom (es llegeix igual al revés).
#
# Especificacions d'entrada:
#   - L'usuari ha d'introduir una paraula.
# ================================================================

paraula = input("Escriu una paraula: ").lower()

if paraula == paraula[::-1]:
    print("És un palíndrom.")
else:
    print("No és un palíndrom.")
