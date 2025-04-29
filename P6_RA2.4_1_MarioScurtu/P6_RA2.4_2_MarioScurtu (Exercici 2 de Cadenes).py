# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Demana una frase i mostra quantes vocals conté.
#
# Especificacions d'entrada:
#   - L'usuari ha d'escriure una frase.
# ================================================================

frase = input("Escriu una frase: ").lower()
vocals = "aeiou"
compte = 0

for lletra in frase:
    if lletra in vocals:
        compte += 1

print("Nombre de vocals:", compte)
