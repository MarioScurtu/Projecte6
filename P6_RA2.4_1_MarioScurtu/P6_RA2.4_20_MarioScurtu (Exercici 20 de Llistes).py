
# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 29/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Mostra només les paraules que comencen per vocal.
#
# Especificacions d'entrada:
#   - L'usuari ha d'escriure paraules separades per espais.
# ================================================================

paraules = input("Escriu paraules separades per espais: ").split()
vocals = "aeiouAEIOU"
filtrades = [p for p in paraules if p[0] in vocals]

print("Paraules que comencen per vocal:", filtrades)
