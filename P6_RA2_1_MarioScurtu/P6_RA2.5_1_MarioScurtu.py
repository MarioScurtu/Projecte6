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
#   Fes un programa el qual donada la data de naixement
#   et calculi la edat i et digui si ets o no major d’edat.
# ================================================================

from datetime import date

any_naixement = int(input("Introdueix l'any de naixement: "))
any_actual = date.today().year

edat = any_actual - any_naixement

print("Tens", edat, "anys.")

if edat >= 18:
    print("Ets major d'edat.")
else:
    print("No ets major d'edat.")

