#tupla

tupla=(1,2,3,4,5)
print(tupla)

tuplasinparentesis=1,2,3,4
print(tuplasinparentesis)

tuplaanidada=1,2,("a","b","c"),3
print(tuplaanidada)

#lista variable de arreglos
listaCD=list("Pundor")
#mutacion
listaLista=[1,2,3,4,5]
tuplaMutada= tuple(listaLista)

tuplaPromedio = (93,97,97,76,99,86)
for i in tuplaPromedio:
    if i > 90:
        print("Felicidades")
    else:
        print("Ponte a juntar latas de aliminio")