# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Mostra els números del 0 fins al número que introdueixi l'usuari.
#
# Especificacions d'entrada:
#   - L'usuari ha de posar un número enter.
# ================================================================

try:
    n = int(input("Introdueix un número: "))
    print(*range(n + 1), sep="\n")
except:
    print("Error: Introdueix un número vàlid.")

