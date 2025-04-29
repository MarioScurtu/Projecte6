# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Mostra els números parells fins al número que posi l'usuari.
#
# Especificacions d'entrada:
#   - L'usuari ha de posar un número enter positiu.
# ================================================================

try:
    n = int(input("Número: "))
    print(*range(0, n + 1, 2), sep="\n")
except:
    print("Error: Introdueix un número vàlid.")
