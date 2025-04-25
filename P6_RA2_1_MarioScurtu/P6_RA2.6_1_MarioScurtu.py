# ================================================================
# Administració d'Aplicacions Informàtiques
# Autor: Mario
# Data: 24/04/2025
# Versió: 1
# ================================================================
# Descripció:
#   Correcció d’un error per mal ordre de crida de funció.
#
# Especificacions de l'entrega:
#   Fes un programa que demani una lletra i et digui si
#   és vocal o consonant.
# ================================================================

lletra = input("Introdueix una lletra: ").lower()

if lletra in ['a', 'e', 'i', 'o', 'u']:
    print("És una vocal.")
else:
    print("És una consonant.")

