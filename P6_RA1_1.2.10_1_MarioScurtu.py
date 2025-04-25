# Administració d'Aplicacions Informàtiques  
# Autor: Mario  
# Data: 24/04/2025  
# Versió: 1  

# Descripció: Fa suma, resta, multiplicació i divisió de dos nombres.
# Especificacions de l'entrega:  Crea una petita calculadora que demani dos números i faci les operacions bàsiques (+, -, *, /).


a = float(input("Introdueix el primer número: "))
b = float(input("Introdueix el segon número: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicació:", a * b)

if b != 0:
    print("Divisió:", a / b)
else:
    print("No es pot dividir per zero.")





