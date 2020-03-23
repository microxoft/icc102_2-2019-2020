def main():
    tCasos = int(input())
    while(tCasos > 0):
        texto1, texto2 = input().split()

        print("Si" if esSubstring(texto2 + texto2, texto1) else "No")

        tCasos -= 1

def esSubstring(texto1, texto2):
    return texto2 in texto1

if(__name__ == "__main__"):
    main()
