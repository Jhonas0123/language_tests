"""el numero es par o impar"""
n1 = int(input("ingrese un numero: "))
op = n1 % 2
if op == 1: 
    print(f"el numero {n1} es impar")
else:
    print(f"el numero {n1} es par")
