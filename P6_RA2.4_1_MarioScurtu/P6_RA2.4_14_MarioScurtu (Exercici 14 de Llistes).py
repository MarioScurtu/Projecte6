
# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Separa 10 números en llistes de parells i senars.
#
# Especificacions d'entrada:
#   - L'usuari ha d'escriure 10 números.
# ================================================================

parells = []
senars = []

for i in range(10):
    num = int(input(f"Número {i+1}: "))
    if num % 2 == 0:
        parells.append(num)
    else:
        senars.append(num)

print("Parells:", parells)
print("Senars:", senars)
