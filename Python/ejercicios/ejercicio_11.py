"""mayor de tres numeros"""
n1 = int(input("ingresa el primer numero: "))
n2 = int(input("ingresa el segundo numero: "))
n3 = int(input("ingresa el tercer numero: "))

if n1 > n2 and n1 > n2:
    print(f"{n1} es el numero mayor de los 3")
elif n2 > n1 and n2 > n3:
    print(f"{n2} es el numero mayor de los 3")
elif n3 > n1 and n3 > n2:
    print(f"{n3} es el numero mayor de los 3")
else:
    print("no existe un numero mayor")