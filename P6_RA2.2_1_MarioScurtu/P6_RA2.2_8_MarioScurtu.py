# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Compta quantes vocals hi ha en una frase introduïda per l’usuari.
#
# Especificacions d'entrada:
#   - L'usuari ha d'introduir una frase.
# ================================================================

frase = input("Introdueix una frase: ")
vocals = "aeiouàèéíòóúü"
comptador = 0

for lletra in frase.lower():
    if lletra in vocals:
        comptador += 1

print("Nombre de vocals:", comptador)








