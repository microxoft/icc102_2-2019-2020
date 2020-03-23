from math import pi

def main():
    problema3()
    
def problema2():
    limS = 1000
    k = 1
    suma = 0

    while(k < limS):
        if(k % 3 == 0 or k % 5 == 0):
            suma += k
        k+=1

    print(suma)

def problema3():
    ladoSolar = int(input())
    ladoBebedero = int(input())
    radioCharca = int(input())/2

    print(ladoSolar**2 - ladoBebedero**2 - pi*radioCharca**2)

if(__name__ == "__main__"):
    main()
