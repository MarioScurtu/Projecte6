# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Calcula el factorial d'un nombre de manera recursiva.
#
# Especificacions d'entrada:
#   - Un nombre enter n.
# Especificacions de sortida:
#   - Retorna el factorial de n.
# ================================================================

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Crides a la funció
print(factorial(0))
print(factorial(3))
print(factorial(5))
