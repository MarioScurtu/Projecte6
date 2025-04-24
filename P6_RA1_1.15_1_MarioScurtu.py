#Administracio....
#Autor: Mario

#Data: 24/04/2025
#Versio: 1

# Descripció: Calcula la velocitat mitjana.  
# Especificacions de l'entrega: L’usuari introdueix distància (km) i temps (h), es calcula velocitat.

print ("Introdueix la distància en quilòmetres: ")
distancia = int(input())

print ("Introdueix el temps en hores: ")
temps = int(input())

velocitat = distancia / temps
print("La velocitat mitjana és:", velocitat, "km/h")