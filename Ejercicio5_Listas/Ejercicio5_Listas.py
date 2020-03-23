def main2():
    lista = []
    cantidad = int(input())

    while(cantidad > 0):
        lista.append(int(input()))
        cantidad -= 1

    print(lista)

def main3():
    lista = []

    valor = int(input())
    while(valor != 0):
        lista.append(valor)

        valor = int(input())

    print(lista)

def main4():
    print(list(map(int, input().split())))

    print([int(val) for val in input().split()])

def cuadrado(val):
    return val**2

def main():
    #lista = [1, 2, 3, 4, 5, 6, 7]
    lista = list(map(int, input().split()))
    print(sum(list(map(cuadrado, lista))))

if(__name__ == "__main__"):
    main()










