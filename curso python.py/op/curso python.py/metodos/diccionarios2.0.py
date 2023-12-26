#creando diccionarios con dict{}
diccionario=dict(nombre="franco",apellido="mariño")
print(diccionario)
#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario={frozenset(["dalto","rancio",]):"jajajja"}
#creando un diccionario con fromkeys() valor por defecto none
diccionario=dict.fromkeys(["nombre","apellido"])
#creando un diccionario con fromkeys() cambiando el valor por defecto a "no se"
diccionario=dict.fromkeys(["nombre","apellido"],"no se")


print(diccionario["apellido"])