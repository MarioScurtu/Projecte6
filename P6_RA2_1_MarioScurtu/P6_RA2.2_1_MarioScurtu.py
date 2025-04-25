# ===================================================================
# Curs: ASIX (Administració de Sistemàtiques en Xarxa)
# Autor: Mario
# Data: 24/04/2025
# Versió: 1
# ===================================================================
# Descripció:
#   Aquest codi demana a l'usuari un número i determina si és parell 
#   o imparell mitjançant l'operador de mòdul (%).
#
# Especificacions d'entrada:
#   - L'usuari ha d'introduir un número enter.
# ===================================================================

num = int(input("Introdueix un número: "))

if num % 2 == 0:
    print("És parell.")
else:
    print("És imparell.")


