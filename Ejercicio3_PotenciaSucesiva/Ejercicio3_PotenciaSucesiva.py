def main():
    print(potencia(2, 4))

def potencia(base, exponente):
    acumuladora = 1
    while(exponente > 0):
        acumuladora *= base
        exponente -= 1
    return acumuladora

def multiplicar(multiplicando1, multiplicando2):
    acumuladora = 0
    if(multiplicando1 > multiplicando2):
        burbuja = multiplicando1
        multiplicando1 = multiplicando2
        multiplicando2 = burbuja
        
    while(multiplicando1 > 0):
        acumuladora += multiplicando2
        multiplicando1 -= 1

    return acumuladora

if(__name__=="__main__"):
    main()
