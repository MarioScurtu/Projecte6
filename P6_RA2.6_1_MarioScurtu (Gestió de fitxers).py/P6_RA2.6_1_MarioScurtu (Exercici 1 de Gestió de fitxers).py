# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Llegeix un fitxer de text anomenat missatge.txt i mostra el seu contingut per pantalla.
#
# Especificacions d'entrada:
#   - Un fitxer de text amb el nom "missatge.txt".
# Especificacions de sortida:
#   - Mostra per pantalla el contingut del fitxer.
# ================================================================

# Obrim el fitxer en mode lectura i mostrem el seu contingut
with open("missatge.txt", "r") as file:
    content = file.read()
    print(content)
