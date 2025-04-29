# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Calcula la suma de tots els nombres des de 1 fins al número
#   introduït per l'usuari. Controla errors si no és un enter positiu.
#
# Especificacions d'entrada:
#   - L'usuari ha d'introduir un número enter positiu.
# ================================================================

try:
    num = int(input("Introdueix un número enter positiu: "))
    if num > 0:
        resultat = sum(range(1, num + 1))
        print("La suma és:", resultat)
    else:
        print("Error: El número ha de ser positiu.")
except ValueError:
    print("Error: No has introduït un número enter vàlid.")
