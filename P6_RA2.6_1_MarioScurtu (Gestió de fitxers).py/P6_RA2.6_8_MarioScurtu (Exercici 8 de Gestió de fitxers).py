# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Llegeix un fitxer que hauria de contenir nombres enters per línia.
#   Si alguna línia no és un enter vàlid, captura l'error i mostra un missatge.
#
# Especificacions d'entrada:
#   - Fitxer "nombres.txt" amb nombres enters.
# Especificacions de sortida:
#   - Mostra un missatge d'error si una línia no és un enter vàlid.
# ================================================================

try:
    with open("nombres.txt", "r") as file:
        for line in file:
            try:
                num = int(line.strip())
                print(f"El número és: {num}")
            except ValueError:
                print(f"Error: '{line.strip()}' no és un número vàlid.")
except FileNotFoundError:
    print("Error: El fitxer 'nombres.txt' no s'ha trobat.")
