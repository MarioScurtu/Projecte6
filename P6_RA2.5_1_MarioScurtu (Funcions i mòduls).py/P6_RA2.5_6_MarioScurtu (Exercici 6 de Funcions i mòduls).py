# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Multiplica tots els números passats com a arguments.
#
# Especificacions d'entrada:
#   - Nombres passats com a arguments a la funció.
# Especificacions de sortida:
#   - Retorna la multiplicació dels números passats.
# ================================================================

def multiplica_tot(*nombres):
    resultat = 1
    for nombre in nombres:
        resultat *= nombre
    return resultat

# Crides a la funció
print(multiplica_tot(2, 3, 4))
print(multiplica_tot(5, 10))
