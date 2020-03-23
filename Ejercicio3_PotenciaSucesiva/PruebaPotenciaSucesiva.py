import libreriaPotencia
from random import randrange
from time import sleep, time

baseNumerica = 10

def main():
    print(libreriaPotencia.potencia(baseNumerica, 3))
    
    minimo = int(input("Digite el mínimo: "))
    maximo = int(input("Digite el máximo: "))
    print(generarAleatorio(minimo, maximo))

def generarAleatorio(min, max):
    return randrange(min, max)

if(__name__ == "__main__"):
    main()
