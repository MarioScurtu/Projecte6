# ===================================================================
# Curs: ASIX (Administració de Sistemàtiques en Xarxa)
# Autor: Mario
# Data: 24/04/2025
# Versió: 1
# ===================================================================
# Descripció:
#   Aquest codi demana a l'usuari tres números i determina quin és el més gran.
#   Utilitza la funció `max()` per trobar el número més gran de les tres entrades.
#
# Especificacions d'entrada:
#   - L'usuari ha d'introduir tres números enters.
# ===================================================================

a = int(input("Introdueix el primer número: "))
b = int(input("Introdueix el segon número: "))
c = int(input("Introdueix el tercer número: "))

maxim = max(a, b, c)

print("El número més gran és:", maxim)


