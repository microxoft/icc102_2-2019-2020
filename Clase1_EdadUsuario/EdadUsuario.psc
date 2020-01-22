Algoritmo EdadUsuario
	Escribir "Escriba su nombre: "
	Leer nombreUsuario
	edad = -1
	Mientras edad<0 Hacer
		Escribir "Escriba su edad: "
		Leer edad
		Si edad<0 Entonces
			Escribir "Error. La edad no puede ser negativa."
		FinSi
	FinMientras
	Escribir "Su nombre es: " nombreUsuario ", y su edad es: " edad " años"
	edad = edad + 10
	Escribir "En 10 años, usted tendrá " edad " años."
FinAlgoritmo

