Algoritmo Ejercicio3_DivisionSucesiva
	dividendo = -1
	Mientras dividendo <= 0 o divisor <= 0 Hacer
		Escribir "Digite el dividendo: "
		Leer dividendo
		Escribir "Digite el divisor: "
		Leer divisor
		Si dividendo <= 0 o divisor <= 0 Entonces
			Escribir "Error. Sólo positivos."
		FinSi
	FinMientras
	cociente = 0
	Mientras dividendo >= divisor Hacer
		cociente = cociente + 1
		dividendo = dividendo - divisor
	FinMientras
	Escribir cociente
FinAlgoritmo

