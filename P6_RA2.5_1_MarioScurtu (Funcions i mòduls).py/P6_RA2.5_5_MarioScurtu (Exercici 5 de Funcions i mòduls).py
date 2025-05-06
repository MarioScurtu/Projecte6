# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Imprimeix "Hola, <nom>" on el nom és un valor donat per l'usuari
#   o "amic" si no s'ha especificat un nom.
#
# Especificacions d'entrada:
#   - Un nom (pot ser per defecte "amic").
# Especificacions de sortida:
#   - Imprimeix "Hola, <nom>".
# ================================================================

def saluda_nom(nom="amic"):
    print(f"Hola, {nom}")

# Crides a la funció
saluda_nom("Joan")
saluda_nom()
saluda_nom("Laia")
