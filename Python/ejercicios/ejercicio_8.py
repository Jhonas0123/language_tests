""" calificaciones 
A = 9 , 10
B = 8
C = 7
D = 6
F = 5 A 0
"""
nota = int(input("ingresa tu nota: "))
if nota >= 0 and nota <= 5:
    print("F")
else:
    if nota == 6:
        print("D")
    else:
        if nota == 7:
            print("C")
        else:
            if nota == 8:
                print("B")
            else:
                if nota >= 9 and nota <= 10:
                    print("A")
                else:
                    print("nota erronea")
