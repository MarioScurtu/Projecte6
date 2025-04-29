# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Mostra la taula de multiplicar d’un número introduït per l’usuari.
#
# Especificacions d'entrada:
#   - L'usuari ha d'introduir un número enter per mostrar la seva taula.
# ================================================================

num = int(input("Introdueix un número enter: "))

print(f"Taula de multiplicar del {num}:")
for i in range(1, 11):
    resultat = num * i
    print(f"{num} x {i} = {resultat}")




