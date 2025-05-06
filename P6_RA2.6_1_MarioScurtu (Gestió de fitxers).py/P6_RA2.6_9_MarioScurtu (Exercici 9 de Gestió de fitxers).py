# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Si un fitxer no existeix, crea'l automàticament i escriu-hi una línia per defecte.
#
# Especificacions d'entrada:
#   - Intent de lectura del fitxer "nou_fitxer.txt".
# Especificacions de sortida:
#   - Si el fitxer no existeix, el crea i escriu "Fitxer creat automàticament".
# ================================================================

try:
    with open("nou_fitxer.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    with open("nou_fitxer.txt", "w") as file:
        file.write("Fitxer creat automàticament")
