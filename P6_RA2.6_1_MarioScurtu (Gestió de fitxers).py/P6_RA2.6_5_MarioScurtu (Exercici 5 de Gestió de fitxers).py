# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Obre un fitxer en mode lectura i escriptura (r+) i afegeix una línia nova sense esborrar
#   el contingut anterior.
#
# Especificacions d'entrada:
#   - Fitxer "dades.txt" amb contingut preexistent.
# Especificacions de sortida:
#   - Mostra el contingut del fitxer i afegeix una línia nova.
# ================================================================

# Obrim el fitxer en mode lectura i escriptura
with open("dades.txt", "r+") as file:
    content = file.read()
    print("Contingut del fitxer abans d'afegir la línia:")
    print(content)
    file.write("\nAfegint una nova línia al final.")
