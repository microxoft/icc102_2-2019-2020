def main():
    valor = -1
    k_Serie = 0
    sum_Serie = 0
    k_Total = 0
    sum_SerieMaxima = 0
    k_SerieMaxima = 0

    while(valor != 0):
        valor = int(input())

        if(valor == 0):
            if(k_Total == k_Serie or sum_Serie > sum_SerieMaxima):
                sum_SerieMaxima = sum_Serie
                k_SerieMaxima = k_Serie
            break

        k_Total += 1

        if(k_Serie == 0 or not esSiguienteElementoSerie(valor, valorAnterior, k_Serie)):
            # Evaluar si esta suma es máxima:
            if(k_Total == k_Serie or sum_Serie > sum_SerieMaxima):
                sum_SerieMaxima = sum_Serie
                k_SerieMaxima = k_Serie
            
            k_Serie = 1
            sum_Serie = valor
        else:
            k_Serie += 1
            sum_Serie += valor

        valorAnterior = valor
        
    print(sum_SerieMaxima / k_SerieMaxima)

def esSiguienteElementoSerie(valor, valorAnterior, k_Potencia):
    return valor == valorAnterior - 2**(k_Potencia-1)

if(__name__ == "__main__"):
    main()








               
