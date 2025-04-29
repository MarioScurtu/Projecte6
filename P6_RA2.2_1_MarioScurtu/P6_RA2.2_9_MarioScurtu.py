# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Troba el valor màxim d’una llista de nombres introduïts per l’usuari.
#
# Especificacions d'entrada:
#   - L'usuari ha d'introduir una llista de nombres separats per espais.
# ================================================================

nombres = input("Introdueix números separats per espais: ").split()
nombres = [int(num) for num in nombres]

maxim = max(nombres)
print("El número màxim és:", maxim)









