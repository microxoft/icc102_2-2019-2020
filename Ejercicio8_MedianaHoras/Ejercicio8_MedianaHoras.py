def main():
    horas = list(map(float, input().split()))

    horas.sort()
    n = len(horas)

    print(horas[int(n/2)] if (n % 2 == 1) else
          (horas[int(n/2)-1] + horas[int(n/2)])/2)


if(__name__=="__main__"):
    main()
