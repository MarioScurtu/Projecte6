# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Mostra una compte enrere de 10 a 1 amb una pausa d’1 segon
#   entre cada número, i després imprimeix "Feliç Any Nou!".
#
# Especificacions d'entrada:
#   - No cal introduir dades per part de l'usuari, sol fa falta 
#     executar la comanda per veure lo que hi ah al codi.
# ================================================================

import time

for numero in range(10, 0, -1):
    print(numero)
    time.sleep(1)

print("Feliç Any Nou!")

