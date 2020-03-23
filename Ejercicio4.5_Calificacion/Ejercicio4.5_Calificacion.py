def main():
    nota = int(input())
    print(calcularCalificacion(nota))

def calcularCalificacion(laNota):
    if(laNota<60):
        return "F"
    elif(laNota<70):
        return "D"
    elif(laNota<80):
        return "C"
    elif(laNota<90):
        return "B"
    else:
        return "A"

if(__name__ == "__main__"):
    main()
