# Ingrid Aldana Torres, Ticiana Passalacqua Gyurkovits
# Escribir un programa que pida al usuario un numero entero que represente un cuadro de ajedrez 

casillas = int(input("Ingrese la cantidad de casillas: "))
numero=1

for i in range (casillas):
    print(f"En el lugar {i+1} hay: {numero}")
    numero = numero * 2
    