#Administracio....
#Autor: Mario

#Data: 24/04/2025
#Versio: 1

# Descripció: Converteix minuts en hores i minuts.  
# Especificacions de l'entrega: L’usuari introdueix un total de minuts i es mostra en format hores:minuts.

print ("Introdueix el nombre de minuts: ")
minuts_totals = int(input())

hores = minuts_totals // 60
minuts = minuts_totals % 60

print(f"Això són {hores} hores i {minuts} minuts.")