def main():
    tCasos = int(input())

    while(tCasos > 0):
        palabraActual = input()

        print("Si" if caracteresUnicos(palabraActual) else "No")

        tCasos -= 1

def caracteresUnicos(palabraActual):
    for posActual, letraActual in enumerate(palabraActual):
        if(letraActual in palabraActual[posActual+1:]):
            return False
    return True

if(__name__ == "__main__"):
    main()
