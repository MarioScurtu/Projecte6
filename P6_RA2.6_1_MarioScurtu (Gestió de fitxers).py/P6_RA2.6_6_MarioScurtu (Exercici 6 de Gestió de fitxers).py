# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Comprova si el fitxer "dades.txt" existeix abans de llegir-lo.
#   Si no existeix, mostra un missatge d'error amigable.
#
# Especificacions d'entrada:
#   - El fitxer "dades.txt" pot existir o no.
# Especificacions de sortida:
#   - Si el fitxer existeix, mostra el contingut. Si no, mostra un missatge d'error.
# ================================================================

import os

# Comprovem si el fitxer existeix
if os.path.exists("dades.txt"):
    with open("dades.txt", "r") as file:
        content = file.read()
        print(content)
else:
    print("Error: El fitxer 'dades.txt' no existeix.")
