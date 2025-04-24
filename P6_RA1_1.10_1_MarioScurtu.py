#Administracio....
#Autor: Mario

#Data: 24/04/2025
#Versio: 1

# Descripció: Compara dues edats i mostra qui és més gran.
# Especificacions de l'entrega: Demana dues edats i indica quina és més gran o si són iguals.

print ("Introdueix la primera edat: ")
edat1 = int(input())

print ("Introdueix la segona edat: ")
edat2 = int(input())

if edat1 > edat2:
    print("La primera persona és més gran.")
elif edat2 > edat1:
    print("La segona persona és més gran.")
else:
    print("Tenen la mateixa edat.")

