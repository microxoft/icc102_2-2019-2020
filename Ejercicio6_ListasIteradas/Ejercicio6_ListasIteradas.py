def buscarValor(lista, valor):
    i = 0
    for valorActual in lista:
        if(valorActual == valor):
            return i
        i+=1
    return -1

listado = [100, 200, 300, 400, 500, 600, 700, 800, 900]
nuevaLista = []

for actual in listado:
    print(actual)
    nuevaLista.append(actual)

print(nuevaLista)

nuevaLista = []

i = 0
while(i < len(listado)):
    print(listado[i])
    nuevaLista.append(listado[i])
    i+=1
print(nuevaLista)

print(buscarValor(nuevaLista, int(input("Valor a buscar:"))))
















