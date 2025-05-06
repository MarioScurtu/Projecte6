# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Afegeix una línia nova a un fitxer existent (sortida.txt) sense esborrar el que ja hi ha.
#
# Especificacions d'entrada:
#   - Fitxer "sortida.txt" que ja conté algunes línies.
# Especificacions de sortida:
#   - Afegim una nova línia al final del fitxer.
# ================================================================

# Obrim el fitxer en mode afegir
with open("sortida.txt", "a") as file:
    file.write("Quarta línia\n")
