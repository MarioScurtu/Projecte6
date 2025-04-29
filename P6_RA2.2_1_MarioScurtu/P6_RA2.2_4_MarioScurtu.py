# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Joc per endevinar un número aleatori entre 1 i 100,
#   amb pistes de "massa alt" o "massa baix".
#
# Especificacions d'entrada:
#   - L'usuari ha d'introduir intents per endevinar el número aleatori.
# ================================================================

import random

secreta = random.randint(1, 100)
intents = 0

while True:
    usuari = int(input("Endevina el número (entre 1 i 100): "))
    intents += 1

    if usuari < secreta:
        print("Massa baix!")
    elif usuari > secreta:
        print("Massa alt!")
    else:
        print(f"Correcte! Has endevinat el número en {intents} intents.")
        break





