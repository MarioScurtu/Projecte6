# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Mostra tots els nombres primers fins al número que posi l'usuari.
#
# Especificacions d'entrada:
#   - L'usuari ha de posar un número enter positiu.
# ================================================================

def es_primer(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

try:
    n = int(input("Número: "))
    for i in range(2, n + 1):
        if es_primer(i):
            print(i)
except:
    print("Error: Introdueix un número vàlid.")
