
# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Demana 5 paraules a l'usuari i les guarda en una llista.
#
# Especificacions d'entrada:
#   - L'usuari ha d'escriure 5 paraules.
# ================================================================

paraules = []
for i in range(5):
    paraula = input(f"Paraula {i+1}: ")
    paraules.append(paraula)

print("Llista de paraules:", paraules)
