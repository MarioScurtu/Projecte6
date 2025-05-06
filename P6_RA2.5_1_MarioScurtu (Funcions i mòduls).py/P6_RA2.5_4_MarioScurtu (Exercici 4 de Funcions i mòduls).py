# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Comprova si els números d'una llista són parells o no.
#
# Especificacions d'entrada:
#   - Llista de números predefinida dins del codi.
# Especificacions de sortida:
#   - Mostra per pantalla si cada número de la llista és parell.
# ================================================================

def es_parell(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]

for num in numeros:
    print(f"El número {num} és parell: {es_parell(num)}")
