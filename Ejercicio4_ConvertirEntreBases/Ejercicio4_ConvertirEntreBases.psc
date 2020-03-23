Algoritmo ConvertirEntreBases
	valorCapturado <- CapturarPositivo()
	baseOrigen = 0
	Mientras baseOrigen < 2 o baseOrigen > 10 Hacer
		Escribir "Indique la base origen: "
		baseOrigen = CapturarPositivo()
	FinMientras
	baseDestino = 0
	Mientras baseDestino < 2 o baseDestino > 10 Hacer
		Escribir "Indique la base destino: "
		baseDestino = CapturarPositivo()
	FinMientras
	Si baseDestino = 10 Entonces
		Escribir ConvertirABase10(valorCapturado, baseOrigen)
	SiNo
		Si baseOrigen = 10 Entonces
			Escribir ConvertirDesdeBase10(valorCapturado, baseDestino)
		SiNo
			Escribir "No se puede hacer esta conversión."
		FinSi
	FinSi
FinAlgoritmo

Funcion resultado <- CapturarPositivo
	resultado <- 0
	Mientras resultado<=0 Hacer
		Escribir 'Digite un valor positivo: '
		Leer resultado
	FinMientras
FinFuncion

Funcion numeroConvertido <- ConvertirABase10(valor, baseOrigen)
	potencia = 1
	Mientras valor>0 Hacer
		numeroConvertido = numeroConvertido + valor%10*potencia
		potencia = potencia * baseOrigen
		valor = trunc(valor / 10)
	FinMientras
FinFuncion

Funcion numeroConvertido <- ConvertirDesdeBase10(valor, baseDestino)
	potencia10 = 1
	numeroConvertido = 0
	Mientras valor > 0 Hacer
		numeroConvertido = numeroConvertido + (valor%baseDestino*potencia10)
		valor = trunc(valor / baseDestino)
		potencia10 = potencia10 * 10
	FinMientras
FinFuncion

