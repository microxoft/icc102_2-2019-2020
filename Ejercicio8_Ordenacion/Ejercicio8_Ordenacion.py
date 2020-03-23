import random

def main():
    A = 10
    B = 1000
    n = int(input("Cantidad de valores a generar: "))
    lista = []

    for i in range(n):
        lista.append(random.randint(A, B))

    print(lista)

    #ordenacionBurbuja(lista)
    #ordenacionSeleccion(lista)
    ordenacionInsercion(lista)

    print(lista)

def ordenacionBurbuja(lista):
    for i in range(0, len(lista)):
        for j in range(0, len(lista)-1-i):
            if(lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista # este retorno no es necesario.

def ordenacionSeleccion(lista):
    for i in range(0, len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        aux = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = aux
    
    return lista # este retorno no es necesario.

def ordenacionInsercion(lista):
    for i in range(1, len(lista)):
        indice = lista[i]
        j = i - 1
        while(j>=0 and lista[j] > indice):
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = indice
    
    return lista # este retorno no es necesario.

if(__name__ == "__main__"):
    main()
