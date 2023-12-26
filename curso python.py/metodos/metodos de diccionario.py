diccionario= {
    "nombre":'franco',
    "apellido":'mariño',
    "subs":100
    }
#devuelve las claves(tambien nos sirve para iterar)
claves=diccionario.keys()
#devuelve el valor de una clave
claves2=diccionario.get("nombre")
#elimina todos los elementos 
#diccionario.clear()
#pop elimina un elemento
diccionario.pop("nombre","subs")
#para iterar el dict
diccionario_iterable=diccionario.items
print(diccionario)