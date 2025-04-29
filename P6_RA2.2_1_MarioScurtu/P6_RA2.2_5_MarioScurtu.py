# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Comprova si un número enter positiu és primer.
#
# Especificacions d'entrada:
#   - L'usuari ha d'introduir un número enter positiu per comprovar-lo.
# ================================================================

num = int(input("Introdueix un número enter positiu: "))

if num < 2:
    print("No és primer.")
else:
    primer = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primer = False
            break
    if primer:
        print("És un nombre primer.")
    else:
        print("No és un nombre primer.")






