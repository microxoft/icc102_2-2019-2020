Algoritmo InvertirNumero
	valor = 0
	Mientras valor<=0 Hacer
		Escribir "Digite un valor positivo: "
		Leer valor
		Si valor <= 0 Entonces
			Escribir "Sólo positivos"
		FinSi
	FinMientras
	resultado = 0
	Mientras valor>0 Hacer
		resultado = resultado * 10
		resultado = resultado + (valor%10)
		valor = trunc(valor / 10)
	FinMientras
	Escribir resultado
FinAlgoritmo

