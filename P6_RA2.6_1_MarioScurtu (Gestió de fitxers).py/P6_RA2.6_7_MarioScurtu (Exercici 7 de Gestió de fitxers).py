# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Intenta escriure en el fitxer "resultats.txt", però gestiona errors d'escriptura
#   com PermissionError si el fitxer és de només lectura o si hi ha permisos denegats.
#
# Especificacions d'entrada:
#   - Un fitxer "resultats.txt" que pot generar errors d'escriptura.
# Especificacions de sortida:
#   - Mostra un missatge d'error si hi ha problemes d'escriptura.
# ================================================================

try:
    with open("resultats.txt", "w") as file:
        file.write("Aquesta és una línia de prova.\n")
except PermissionError:
    print("Error: No tens permís per escriure al fitxer.")
