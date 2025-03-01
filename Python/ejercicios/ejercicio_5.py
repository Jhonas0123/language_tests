n1 = int(input("ingresa el primer numero: "))
n2 = int(input("ingresa el segundo numero: "))
menu = int(input(f"""Selecciona una opcion del MENU:
1. SUMA
2. RESTA
3. MULTIPLICAR
4. DIVISION
5. SALIR
"""))
if menu == 1:
    print(f"suma: {n1+n2}")
elif menu == 2:
    print(f"resta: {n1-n2}")
elif menu == 3:
    print(f"multiplicacion: {n1*n2}")
elif menu == 4:
    print(f"division: {n1/n2}")
elif menu == 5:
    print("Hasta pronto")
else:
    print("operacion erronea")
