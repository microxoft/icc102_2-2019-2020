def main():
    valorCapturado = CapturarPositivo()

    baseOrigen = 0
    while(baseOrigen < 2 or baseOrigen > 10):
        print("Indique la base origen:")
        baseOrigen = CapturarPositivo()

    baseDestino = 0
    while(baseDestino < 2 or baseDestino > 10):
        print("Indique la base destino:")
        baseDestino = CapturarPositivo()

    if(baseDestino == 10):
        print(ConvertirABase10(valorCapturado, baseOrigen))
    elif(baseOrigen == 10):
        print(ConvertirDesdeBase10(valorCapturado, baseDestino))
    else:
        print("No se puede hacer esta conversión.")

def CapturarPositivo():
    resultado = 0
    while(resultado <= 0):
        resultado = int(input("Digite un valor positivo:"))

        if(resultado <= 0):
            print("Sólo positivos.")
    return resultado

def ConvertirABase10(valor, baseOrigen):
    potencia = 1
    numeroConvertido = 0
    
    while(valor>0):
        numeroConvertido += valor%10 * potencia
        potencia *= baseOrigen
        valor //= 10
        
    return numeroConvertido

def ConvertirDesdeBase10(valor, baseDestino):
    potencia10 = 1
    numeroConvertido = 0

    while(valor > 0):
        numeroConvertido += (valor % baseDestino * potencia10)
        valor //= baseDestino
        potencia10 *= 10

    return numeroConvertido

if(__name__ == "__main__"):
    main()





























