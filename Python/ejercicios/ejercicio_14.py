""" ciclo de repetir hasta """
""" pedir un numero de dos digitos """


numero = int(input("ingrese un numero de 2 digitos: "))

while numero <= 10 or numero >=99:
    numero = int(input("ingrese un numero de 2 digitos: "))
else:
    print(f"el numero ingresado es de dos digitos y es {numero}")

