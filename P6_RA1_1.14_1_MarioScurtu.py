#Administracio....
#Autor: Mario

#Data: 24/04/2025
#Versio: 1

# Descripció: Calcula el preu amb IVA d’un producte.  
# Especificacions de l'entrega: L’usuari introdueix el preu base i es calcula amb un 21% d’IVA.

print ("Introdueix el preu del producte: ")
preu_base = int(input())
iva = preu_base * 0.21
preu_final = preu_base + iva
print("El preu amb IVA és:", preu_final)