def main():
    listado = list(map(int, input().split()))

    opcionMenu = -1

    while(opcionMenu != 0):
        opcionMenu = mostrarMenu(listado)

        if(opcionMenu == 1):
            j = int(input("Digite el valor de J: "))

            print(obtenerUltimosValores(listado, j))
        elif(opcionMenu == 2):
            invertirLista(listado)
            print(listado)
        elif(opcionMenu == 3):
            desde = int(input("Desde: "))
            hasta = int(input("Hasta: "))
            step = int(input("Saltos: "))
            print(obtenerSubconjunto(listado, desde, hasta, step))
        elif(opcionMenu == 4):
            posicion = int(input("Posición: "))

            print(obtenerElemento(listado, posicion))
        elif(opcionMenu == 5):
            elemento = int(input("Elemento: "))

            print(obtenerPosicion(listado, elemento))
        elif(opcionMenu == 6):
            opcionSubmenu = MostrarSubMenu(listado)

            while(opcionSubmenu != 0):
                if(opcionSubmenu == 1):
                    elemento = int(input("Elemento: "))
                    agregarElemento(listado, elemento, len(listado))
                elif(opcionSubmenu == 2):
                    elemento = int(input("Elemento: "))
                    agregarElemento(listado, elemento, 0)
                elif(opcionSubmenu == 3):
                    elemento = int(input("Elemento: "))
                    posicion = int(input("Posición: "))
                    agregarElemento(listado, elemento, posicion)
                elif(opcionSubmenu == 4):
                    nuevaLista = list(map(int, input("Digite la nueva lista").split()))
                    extenderLista(listado, nuevaLista)
                elif(opcionSubmenu == 5):
                    posicion = int(input("Posición: "))
                    eliminarPosicion(listado, posicion)
                elif(opcionSubmenu == 6):
                    elemento = int(input("Elemento: "))
                    eliminarElemento(listado, elemento)

                opcionSubmenu = MostrarSubMenu(listado)

def eliminarElemento(listado, elemento):
    listado.remove(elemento)

def eliminarPosicion(listado, posicion):
    #del(listado[posicion])
    listado.pop(posicion)

def extenderLista(listado, nuevaLista):
    listado.extend(nuevaLista)

def agregarElemento(listado, elemento, posicion):
    listado.insert(posicion, elemento)

def MostrarSubMenu(listado):
    print(f"Valores: {listado} (longitud: {len(listado)})")

    print("1: Agregar elemento al final.")
    print("2: Agregar elemento al inicio.")
    print("3: Agregar elemento en una posición Y.")
    print("4: Extender la lista al inicio o final.")
    print("5: Eliminar posición.")
    print("6: Eliminar elemento.")
    print("\n0: Salir.")

    return int(input())

def obtenerPosicion(listado, elemento):
    return listado.index(elemento)

def obtenerElemento(listado, posicion):
    return listado[posicion]

def obtenerSubconjunto(listado, desde, hasta, step):
    return listado[desde:hasta:step]

def invertirLista(listado):
    listado.reverse()

def obtenerUltimosValores(listado, j):
    return listado[:len(listado)-j-1:-1]

def mostrarMenu(listado):
    print(f"Valores: {listado} (longitud: {len(listado)})")

    print("1: Sacar los últimos J valores.")
    print("2: Mostrar la lista invertida.")
    print("3: Mostrar sub-conjunto.")
    print("4: Mostrar elemento en posición X.")
    print("5: Ubicar elemento.")
    print("6: Modificar la lista.")
    print("\n0: Salir.")

    return int(input())

if(__name__ == "__main__"):
    main()
