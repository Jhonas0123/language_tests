"""etapas de la vida"""
edad = int(input("ingresa tu edad: "))
if edad >= 0 and edad <= 10:
    print("eres joven")
else:
    if edad >= 11 and edad <= 20:
        print("eres un semi adulto")
    else:
        if edad >= 21 and edad <= 30:
            print("chale ya eres adulto")
        else:
            print("edad invalida")
        