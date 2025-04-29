
# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Elimina duplicats d'una llista.
#
# Especificacions d'entrada:
#   - No cal entrada de l'usuari. La llista ja està definida.
# ================================================================

llista = [1, 2, 2, 3, 4, 4, 5]
sense_duplicats = list(set(llista))
print("Sense duplicats:", sense_duplicats)
