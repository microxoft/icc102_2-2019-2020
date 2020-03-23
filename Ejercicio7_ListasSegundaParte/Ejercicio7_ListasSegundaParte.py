def main():
    frase = input()
    fraseInversa = list(frase).copy()
    fraseInversa.reverse()

    if(list(frase) == fraseInversa):
        print("Sí")
    else:
        print("No")

    if(esPalindroma2(frase)):
        print("Es palíndroma")
    else:
        print("No es palíndroma")

    

def esPalindroma(texto):
    limI = 0
    limS = len(texto) - 1

    while(limI < limS):
        if(texto[limI] != texto[limS]):
            return False

        limI += 1
        limS -= 1

    return True

def esPalindroma2(texto):
    texto = texto.lower()
    limI = 0
    limS = len(texto) - 1

    while(limI < limS):
        while(texto[limI] == " "):
            limI += 1
        while(texto[limS] == " "):
            limS -= 1

        if(limI >= limS):
            return True

        if(texto[limI] != texto[limS]):
            return False

        limI += 1
        limS -= 1

    return True


if(__name__ == "__main__"):
    main()













    
