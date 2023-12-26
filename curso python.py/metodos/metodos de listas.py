#creando una lista con list()
lista=list(["hola","capo",45,True])
#devuelve la cantidad de elementos de la lista
cantidad_de_elementos= len(lista)
#agregando un elemento a la lista
lista.append("jajajaj") 
#agregando un elemento a la lista en un indice especifico
lista.insert(2,"toma mama")
#agregando varios elementos a la lista
lista.extend([False,"blue"])
#eliminando elementos de la lista por su indice
lista.pop(0)
#removiendo un elemento de la lista por su valor
lista.remove("toma mama")
#eliminando los elementos de la lista
lista.clear()
#ordena los elementos de la lista de menor  mayor(no funciona con string)
lista.sort()
#da vuelta todos los elementos de la lista
lista.reverse
#verifica si un elemento esta en la lista
elemento_encontrado=lista.index(45)
print(elemento_encontrado)
