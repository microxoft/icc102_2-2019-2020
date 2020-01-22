print("Escriba su nombre: ")
nombreUsuario = input()
edad = -1

while(edad < 0):
    print("Escriba su edad: ")
    edad = int(input())

    if edad < 0:
        print("Error. La edad no puede ser negativa.")

print("Su nombre es: " + nombreUsuario + ", y su edad es: " + str(edad) + " años")
edad = edad + 10
print("En 10 años, usted tendrá " + str(edad) + " años.")
