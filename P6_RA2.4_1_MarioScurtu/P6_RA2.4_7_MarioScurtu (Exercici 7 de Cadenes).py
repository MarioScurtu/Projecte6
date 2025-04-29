# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Compta quantes vegades apareix una lletra dins d'una cadena.
#
# Especificacions d'entrada:
#   - L'usuari ha d'introduir una cadena i una lletra.
# ================================================================

cadena = input("Escriu una cadena: ")
lletra = input("Quina lletra vols comptar? ")

compte = cadena.count(lletra)
print(f"La lletra '{lletra}' apareix {compte} vegades.")
