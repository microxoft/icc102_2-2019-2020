def main():
    valores = list(map(int, input().split()))
    pivoteX = int(input())
    print(particionar(valores, pivoteX))
    
def particionar(valores, pivoteX):
    particion = 0
    for posActual, valorActual in enumerate(valores):
        if(valores[posActual] < pivoteX):
            burbuja = valores[posActual]
            valores[posActual] = valores[particion]
            valores[particion] = burbuja

            particion += 1
    return valores

if(__name__ == "__main__"):
    main()
