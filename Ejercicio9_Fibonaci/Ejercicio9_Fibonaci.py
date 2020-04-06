def main():
    print(fibRec(int(input())))
    return

def fib(n):
    n -= 1
    primer = 0
    segundo = 1
    tercer = 1
    k = 0

    while(k < n):
        tercer = primer + segundo
        primer = segundo
        segundo = tercer

        k += 1

    if(n <= 0):
        return n+1
    else:
        return segundo

def fibRec(n):
    if(n <= 1):
        return n

    return fibRec(n-1) + fibRec(n-2)

if(__name__ == "__main__"):
    main()
