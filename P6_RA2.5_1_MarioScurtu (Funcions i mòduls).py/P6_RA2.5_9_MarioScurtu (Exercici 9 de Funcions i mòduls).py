# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Determina l'estat d'una persona segons la seva edat.
#   Els estats possibles són "Menor d'edat", "Adult" o "Jubilat".
#
# Especificacions d'entrada:
#   - Una edat de la persona.
# Especificacions de sortida:
#   - Retorna l'estat i una descripció de l'edat.
# ================================================================

def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat", "Són menors de 18 anys."
    elif 18 <= edat < 65:
        return "Adult", "Són adults, amb més de 18 anys."
    else:
        return "Jubilat", "Persones amb més de 65 anys."

# Crides a la funció
print(estat_persona(12))
print(estat_persona(25))
print(estat_persona(70))
