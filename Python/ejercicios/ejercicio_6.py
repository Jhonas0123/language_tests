"""meses del año
12, 1, 2 = estacion de invierno
3, 4, 5 = primavera
6, 7, 8 = verano
9, 10, 11= otoño"""

mes = int(input("ingresa el numero del mes: "))
if mes == 12 or  mes ==  1 or  mes ==  2:
    print(f"El mes {mes} esta en estacion de invierno")
elif mes == 3 or  mes ==  4 or  mes ==  5:
    print(f"El mes {mes} esta en estacion de primavera")
elif mes == 6 or  mes ==  7 or  mes ==  8:
    print(f"El mes {mes} esta en estacion de verano")
elif mes == 9 or  mes ==  10 or  mes == 11:
    print(f"El mes {mes} esta en estacion de otoño")
else:
    print("este mes no existe") 