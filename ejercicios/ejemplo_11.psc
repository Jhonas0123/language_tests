Algoritmo switch
	Definir num1, num2, res Como Real
	ESCRIBIR "primer numeros"
	leer num1, num2
	escribir "digite que opcion quiere seguir"
	escribir "1 = suma, 2 = resta, 3 = multiplicacion, 4 = division"
	leer numero
	Segun numero Hacer
		1:
			res = num1 + num2
			escribir "la suma es ", res
		2:
			res = num1 - num2
			escribir "la resta es ", res
		3:
			res = num1 * num2
			escribir "la multiplicacion es ", res
		4:
			res = num1 / num2
			escribir "la division es ", res
		De Otro Modo:
			escribir "error al colocar la opcion"
	Fin Segun
	
	
FinAlgoritmo
