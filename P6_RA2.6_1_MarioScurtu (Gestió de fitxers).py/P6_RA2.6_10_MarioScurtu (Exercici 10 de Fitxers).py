# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 06/05/2025
# Versió: 1
# ================================================================
# Descripció:
#   Simula una lectura d'un fitxer assegurant que el fitxer es tanqui
#   encara que hi hagi un error.
#
# Especificacions d'entrada:
#   - Fitxer de text que podria contenir dades errònies o provocar errors.
# Especificacions de sortida:
#   - Missatge d'error (si n'hi ha) i comprovació que el fitxer es tanca correctament.
# ================================================================

try:
    fitxer = open("fitxer_dades.txt", "r")
    contingut = fitxer.read()
    print("Contingut del fitxer:", contingut)
    # Provocar un error voluntàriament (per exemple dividir per zero)
    resultat = 10 / 0
except ZeroDivisionError:
    print("S'ha produït un error en processar les dades (divisió per zero).")
except FileNotFoundError:
    print("El fitxer no existeix.")
finally:
    try:
        fitxer.close()
        print("El fitxer s'ha tancat correctament.")
    except NameError:
        print("El fitxer no s'ha pogut obrir, per tant no cal tancar-lo.")
