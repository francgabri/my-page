#le pedimos al usuario que nos diga una frase (o varias)
frase=input("decime una frase y te calculo cuanto tardas si tuvieras que decirla:")
#creamos una lista con todas las palabras de la frase(se separan cada vez que haya un estado en blanco)
palabras_separadas=frase.split(" ")
#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras=len(palabras_separadas)
#calculamos la cantidad de palabras y le decimos
print(f"dijiste {cantidad_de_palabras} palabras,y tardaras {cantidad_de_palabras/2} segundos decirlo")
print(f"dalto lo diria en {cantidad_de_palabras*100//2*1.3/100} segundos")
#en caso de que tarde mas de un minuto le decimos que pare
if cantidad_de_palabras >120:
 print("para flaco tampoco te pedi un testamento")