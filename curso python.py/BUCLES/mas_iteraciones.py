frutas=["banana","ciruela","naranja","anana","manzana"]
cadena="hola franco"
numeros=[2,6,4,9]
#evitando que se coma una naranja con continue
for fruta in frutas:
    if fruta == "naranja":
        continue
    print(f"me voy a comer una {fruta}")
    
#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    if fruta == "anana":
        break
    print(f"me voy a comer una {fruta}")
else:
    print("se cierra el bucle")

#recorrer una cadena de texto

for letra in cadena:
    print(letra)

#for de una manera ineficiente
numeros_duplicados=list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
print(numeros_duplicados)

#for en una sola linea de codigo(duplicamos los numeros)
numeros_duplicados=[x*2 for x in numeros]
print(numeros_duplicados)