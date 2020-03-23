import sys

def main():
    lista = list(map(int, input("Digite la lista").split()))
    aBuscar = int(input("Digite el valor a buscar: "))

    #print(sys.getsizeof(aBuscar))

    posicion = busquedaSec(lista, aBuscar)
    if(posicion >= 0):
        print(f"Encontrado en {posicion}")
    else:
        print("No existe.")

    posicion = busquedaBin(lista, aBuscar)
    if(posicion >= 0):
        print(f"Encontrado en {posicion}")
    else:
        print("No existe.")

def busquedaSec(lista, elemento):
    i = 0
    while(i < len(lista) and lista[i] != elemento):
        i+=1

    return i if i < len(lista) else -1

def busquedaBin(lista, elemento):
    limI = 0
    limS = len(lista) - 1

    while(limI<=limS):
        posicionCentral = int(limI/2 + limS/2)

        if(elemento < lista[posicionCentral]):
            limS = posicionCentral - 1
        elif(elemento > lista[posicionCentral]):
            limI = posicionCentral + 1
        else:
            return posicionCentral
    return -1

if(__name__ == "__main__"):
    main()

















