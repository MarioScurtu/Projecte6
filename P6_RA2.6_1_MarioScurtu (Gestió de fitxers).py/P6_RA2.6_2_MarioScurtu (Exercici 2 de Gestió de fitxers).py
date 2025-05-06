# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Escriu tres línies en un fitxer anomenat sortida.txt.
#   El contingut anterior (si n'hi ha) s'esborrarà.
#
# Especificacions d'entrada:
#   - Es crea el fitxer "sortida.txt" amb el contingut següent:
#     - "Primera línia"
#     - "Segona línia"
#     - "Tercera línia"
# Especificacions de sortida:
#   - El fitxer es sobreescriurà amb aquest contingut.
# ================================================================

# Obrim el fitxer en mode escriptura per sobreescriure'l
with open("sortida.txt", "w") as file:
    file.write("Primera línia\n")
    file.write("Segona línia\n")
    file.write("Tercera línia\n")
