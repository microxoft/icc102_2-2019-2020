from math import sqrt

def main():
    n = int(input())
    x = int(input())

    m = n
    suma = 0
    sumaImpares = 0
    sumaPrimos = 0
    cantidadXDigitos = 0
    elMayor = 0
    elMenor = 0

    while(m>0):
        valorActual = int(input())

        if(esElMayor(valorActual, elMayor) or m==n):
            elMayor = valorActual

        if(esElMenor(valorActual, elMenor) or m==n):
            elMenor = valorActual

        suma += valorActual

        if(esImpar(valorActual)):
            sumaImpares += valorActual

        if(esPrimo(valorActual)):
            sumaPrimos += valorActual

        if(tieneXDigitos(valorActual, x)):
            cantidadXDigitos += 1

        m -= 1

    print(elMayor)
    print(elMenor)
    print(suma/n)
    print(sumaImpares)
    print(sumaPrimos)
    print(cantidadXDigitos)

def esElMayor(nuevo, viejoMayor):
    return nuevo>viejoMayor

def esElMenor(nuevo, viejoMenor):
    return nuevo<viejoMenor

def esImpar(valor):
    return valor%2 != 0

def esPrimo(valorActual):
    k = 2

    while(k<=sqrt(valorActual)):
        if(valorActual%k == 0):
            return False
        k+=1
    return True

def tieneXDigitos(elValor, x):
    potencia = 10**x
    return elValor<potencia and elValor>=10**(x-1)

if(__name__ == "__main__"):
    main()















    
