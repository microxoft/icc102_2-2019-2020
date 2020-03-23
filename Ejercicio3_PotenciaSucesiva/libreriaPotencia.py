def main():
    print(potencia(2, 4))

def potencia(base, exponente):
    acumuladora = 1
    while(exponente > 0):
        acumuladora *= base
        exponente -= 1
    return acumuladora

def multiplicar(multiplicando1, multiplicando2):
    acumuladora = 0
    if(multiplicando1 > multiplicando2):
        burbuja = multiplicando1
        multiplicando1 = multiplicando2
        multiplicando2 = burbuja
        
    while(multiplicando1 > 0):
        acumuladora += multiplicando2
        multiplicando1 -= 1

    return acumuladora

if(__name__=="__main__"):
    main()


"¡Hola " + "mundo!"
# => "¡Hola mundo!"

"¡Hola " "mundo!"
# => "¡Hola mundo!"

"Esta es una cadena"[0]
# => 'E'

len("Esta es una cadena")
# => 18

"Las {} pueden ser {}".format("Cadenas", "interpoladas")
# => "Las Cadenas pueden ser interpoladas"

"Subí la loma, {0}, volví y bajé, {0}".format("¡Ombe!")
# => "Subí la loma, ¡Ombe!, volví y bajé, ¡Ombe!"

"{nombre} quiere comer {comida}".format(name="Miguel", food="pizza")
# => "Miguel quiere comer pizza"

"%s pueden %s a la %s" % ("Cadenas", "interpolarse", "antigua")
# => "Cadenas pueden interpolarse a la antigua"

# You can also format using f-strings or formatted string literals (in Python 3.6+)
nombre = "Miguel"
f"Él dijo que su nombre es {nombre}."
# => "Él dijo que su nombre es Miguel"

f"{nombre} tiene {len(nombre)} letras."
# => "Miguel tiene 6 letras."



if(condición/expresión):
    instrucción(es)




if(n2>n1):
    burbuja = n2
    n2 = n1
    n1 = burbuja






if(condición/expresión):
    instrucción(es)
elif(condición/expresión):
    instrucción(es)
else:
    instrucción(es)







if(esPar(numero)):
    print("Es par")
    cantidadPares += 1
else:
    print("Es impar")
    sumaImpares += numero
    cantidadImpares += 1




animales = ["perro", "gato", "ratón"]
for i, valor in enumerate(animales):
    print(i, valor)





for valor in colección:
    instrucción(es)




while(condición):
    instrucción(es)





x = 0
while x < 4:
    print(x)
    x += 1






for i in range(1, 900000):
    print(i)
    if i >= 30:
        break







numero = -1
while(numero != 0):
    numero = int(input("Valor: "))

    if(numero == 0):
        break;





i = 0
sumaFactores = 0
while(i < a/2):
    i+=1
    if(a%i != 0):
        print(f"No es factor: {i}")
        continue
    print(f"Es factor: {i}")
    sumaFactores += i




