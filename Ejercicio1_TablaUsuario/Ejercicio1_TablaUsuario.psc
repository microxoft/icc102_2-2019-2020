Algoritmo TablaUsuario
	tabla = 0
	Mientras tabla < 1 o tabla > 12 Hacer
		Escribir "Especifique la tabla (del 1 al 12): "
		Leer tabla
	FinMientras
	inferior = 1
	superior = 10
	acumulado = 0
	Mientras inferior<=superior Hacer
		Escribir tabla, " x ", inferior, " = ‰", tabla*inferior
		acumulado = acumulado + tabla*inferior
		inferior = inferior + 1
	FinMientras
	Escribir acumulado
FinAlgoritmo

