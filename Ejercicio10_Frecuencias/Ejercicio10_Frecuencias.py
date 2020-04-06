def main():
    casos = int(input())

    while(casos > 0):
        frecuencias = input()
        equivalencias = input()
        dictFrecuencias = nombresReales(equivalencias)

        print(dictFrecuencias)
        #for frecActual in frecuencias.split(','):
        #    dictFrecuencias[nombreReal(frecActual.split(':')[0])] = int(frecActual.split(':')[1])

        

        print(dictFrecuencias)
        
        casos -= 1

def nombresReales(equivalencias):
    dictReales = {}
    for equivalenciaActual in equivalencias.split(','):
        Existe = True
        
        Existe = equivalenciaActual.split(':')[1] in dictReales

        if(Existe):
            dictReales[equivalenciaActual.split(':')[1]].append(equivalenciaActual.split(':')[0])
        else:
            dictReales[equivalenciaActual.split(':')[1]] = list(equivalenciaActual.split(':')[0])

    return dictReales
                

if(__name__ == "__main__"):
    main()
