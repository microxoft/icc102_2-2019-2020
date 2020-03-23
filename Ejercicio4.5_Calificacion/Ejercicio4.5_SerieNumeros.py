Algoritmo SerieNumeros
	Leer n
	Leer x
	// Guardamos una copia de n, para calcular el promedio.
	m <- n
	suma <- 0
	sumaImpares <- 0
	sumaPrimos <- 0
	cantidadXDigitos <- 0
	elMayor <- 0
	elMenor <- 0
	Mientras m>0 Hacer
		Leer valorActual
		Si esElMayor(valorActual,elMayor) O m=n Entonces
			elMayor <- valorActual
		FinSi
		Si esElMenor(valorActual,elMenor) O m=n Entonces
			elMenor <- valorActual
		FinSi
		suma <- suma+valorActual
		Si esImpar(valorActual) Entonces
			sumaImpares <- sumaImpares+valorActual
		FinSi
		Si esPrimo(valorActual) Entonces
			sumaPrimos <- sumaPrimos+valorActual
		FinSi
		Si tieneXDigitos[valorActual,x] Entonces
			cantidadXDigitos <- cantidadXDigitos+1
		FinSi
		m <- m-1
	FinMientras
	Escribir elMayor
	Escribir elMenor
	Escribir suma/n
	Escribir sumaImpares
	Escribir sumaPrimos
	Escribir cantidadXDigitos
FinAlgoritmo

Funcion resultado <- esElMayor(nuevo,viejoMayor)
	Si nuevo>viejoMayor Entonces
		resultado <- verdadero
	SiNo
		resultado <- falso
	FinSi
FinFuncion

Funcion resultado <- esElMenor(nuevo,viejoMenor)
	Si nuevo<viejoMenor Entonces
		resultado <- verdadero
	SiNo
		resultado <- falso
	FinSi
FinFuncion

Funcion result <- esImpar(valor)
	Si valor MOD 2=0 Entonces
		result <- falso
	SiNo
		result <- verdadero
	FinSi
FinFuncion

Funcion res <- esPrimo(valorActual)
	k <- 2
	Mientras k<=rc(valorActual) Hacer
		Si valorActual MOD k=0 Entonces
			res <- falso
		FinSi
		k <- k+1
	FinMientras
	res <- verdadero
FinFuncion

Funcion resultado <- tieneXDigitos(elValor, x)
	potencia = 10^x
	Si elValor<potencia y elValor>=10^(x-1) Entonces
		resultado = verdadero
	SiNo
		resultado = falso
	FinSi
FinFuncion

