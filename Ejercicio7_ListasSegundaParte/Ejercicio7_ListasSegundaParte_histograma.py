from math import ceil

def main():
    valores = list(map(int, input().split()))
    print(valores)
    valores = generarProporciones(valores)
    print(valores)
    generarHistograma(valores)

def generarProporciones(vals):
    resultado = []
    
    for valorActual in vals:
        resultado.append(ceil(valorActual / sum(vals) * 100))

    return resultado

def generarHistograma(listado):
    for val in listado:
        print(f"{val}%", end='\t')
        while(val > 0):
            print("█", end='')
            val -= 1
        print()

if(__name__ == "__main__"):
    main()
