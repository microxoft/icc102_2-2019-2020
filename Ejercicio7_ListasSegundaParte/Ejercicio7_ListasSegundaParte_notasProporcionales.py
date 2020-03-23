from random import randrange

def main():
    #notas = list(map(int, input().split()))
    notas = []
    n = 20
    while(n > 0):
        notas.append(randrange(0, 71))
        n -= 1
    notas.sort()

    print(f"El promedio es: {sum(notas) / len(notas)}")

    notasProporcionales = generarProporciones(notas)

    mostrarTablaProporciones(notas, notasProporcionales)

    limiteInferior = int(input())
    limiteSuperior = int(input())

    filtradas = filtrarProporcion(notas,
                                  notasProporcionales,
                                  limiteInferior,
                                  limiteSuperior)

    print(f"Notas: {filtradas}\tCantidad: {len(filtradas)}")

def filtrarProporcion(notas,
                      notasProporc,
                      limiteInferior,
                      limiteSuperior):
    resultado = []

    for i, proporcionActual in enumerate(notasProporc):
        if(proporcionActual >= limiteInferior and
           proporcionActual <= limiteSuperior):
            resultado.append(notas[i])

    return resultado

def mostrarTablaProporciones(notas, notasProporcionales):
    for i, notaActual in enumerate(notas):
        print(f"{notaActual}\t{notasProporcionales[i]}")

def generarProporciones(notas):
    resultado = []

    for notaActual in notas:
        resultado.append(notaActual / 70 * 100)

    return resultado

if(__name__ == "__main__"):
    main()
