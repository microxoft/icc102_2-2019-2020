Algoritmo ResiduoSucesivo
	dividendo = -1
	divisor = -1
	Mientras dividendo<=0 o divisor<=0 Hacer
		Escribir "Digite el dividendo: "
		Leer dividendo
		Escribir "Digite el divisor: "
		Leer divisor
		Si dividendo <= 0 o divisor <= 0 Entonces
			Escribir "Error. Solo positivos."
		FinSi
	FinMientras
	Mientras dividendo >= divisor Hacer
		dividendo = dividendo - divisor
	FinMientras
	Escribir dividendo
FinAlgoritmo

