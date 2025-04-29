# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Mostra la taula de multiplicar del número que introdueixi l'usuari.
#
# Especificacions d'entrada:
#   - L'usuari ha de posar un número enter.
# ================================================================

try:
    n = int(input("Número: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
except:
    print("Error: Introdueix un número vàlid.")


