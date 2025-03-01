vacaciones = input("tienes vacaciones? V o F: ")
dia_descanso = input("tienes dia de descanso? V o F: ")

if vacaciones or dia_descanso:
    print("puede asistir al juego de su hijo")
else:
    print("tiene deberes que hacer")