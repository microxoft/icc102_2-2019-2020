def main():
    valor = capturarPositivo()
    print(Invertir(valor))

def capturarPositivo():
    valor = 0
    while(valor<=0):
        valor = int(input("Digite un valor positivo: "))
        if(valor <= 0):
            print("Sólo positivos.")
    return valor

def Invertir(numero):
    resultado = 0

    while(numero > 0):
        resultado *= 10
        resultado += (numero%10)
        numero //= 10

    return resultado

if(__name__ == "__main__"):
    main()
