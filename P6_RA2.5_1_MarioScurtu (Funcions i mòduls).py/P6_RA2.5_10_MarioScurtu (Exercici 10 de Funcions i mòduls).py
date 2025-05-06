# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Filtra els números parells d'una llista.
#
# Especificacions d'entrada:
#   - Una llista de nombres.
# Especificacions de sortida:
#   - Retorna una nova llista amb només els números parells.
# ================================================================

def filtra_parells(llista):
    return [num for num in llista if num % 2 == 0]

# Crides a la funció
print(filtra_parells([1, 2, 3, 4, 5, 6]))
print(filtra_parells([10, 15, 20, 25, 30]))
