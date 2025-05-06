# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Llegeix un fitxer i compta quantes línies té.
#
# Especificacions d'entrada:
#   - Fitxer "missatge.txt" amb diverses línies de text.
# Especificacions de sortida:
#   - Mostra per pantalla el nombre de línies del fitxer.
# ================================================================

# Obrim el fitxer en mode lectura i comptem les línies
with open("missatge.txt", "r") as file:
    lines = file.readlines()
    print(f"El fitxer té {len(lines)} línies.")
