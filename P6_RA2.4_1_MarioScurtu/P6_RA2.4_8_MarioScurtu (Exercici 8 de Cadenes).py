# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Elimina tots els espais d'una cadena.
#
# Especificacions d'entrada:
#   - L'usuari ha d'escriure una cadena amb espais.
# ================================================================

text = input("Escriu una frase: ")
sense_espais = text.replace(" ", "")
print("Frase sense espais:", sense_espais)
