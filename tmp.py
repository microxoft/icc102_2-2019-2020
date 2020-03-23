


#li = [ele1, ele2, ele3, ...]





#li1.append(elemento)
#li2.insert(posición, elemento)





li1 = [18, 23, 21, 22, 18, 20]
li2 = ["José", "Miguel", "Pablo"]





li1.append(24)
li2.insert(2, "Juan")







#listaDestino.extend(listaOrigen)









li1.extend(li2)




#lista.pop(índice)
#lista.remove(elemento)
#del(lista[índice])





li1.pop()
li1.pop(8)
li1.remove("José")
del(li1[7])





#lista.index(elemento[, inicio[, fin]])






#print(li2.index("Pablo"))





#lista.reverse()







li1.reverse()





#lista.sort([key=None], [reverse=False])



def miFuncion(valor):
    return len(valor)

li1.sort()
print(li1)
li1.sort(reverse=True)
print(li1)
li2.sort(key=miFuncion)
print(li2)





#lista.count(valor)
#len(lista)







print(li1.count(18))
print(len(li1))
print(len(li2))





#sum(lista)
#max(lista)
#min(lista)




print(sum(li1))
print(max(li1))
print(min(li1))




