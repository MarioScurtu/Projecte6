# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Mostra els 10 primers termes de la seqüència de Fibonacci.
#
# Especificacions d'entrada:
#   - No cal introduir dades per part de l'usuari, sol fa falta 
#     executar la comanda per veure lo que hi ah al codi.
# ================================================================

a, b = 0, 1
print("Primers 10 termes de Fibonacci:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()







