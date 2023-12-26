animales={"gato","perro","loro","cocodrilo"}
numeros={33,45,67,29}

#recorriendo la conjunto animales
for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")
#recorriendo la conjunto de numeros y multiplicandola por 10
for numero in numeros:
    resultado=numero*10
    print(resultado)
#reccorriendo dos conjuntos del mismo tamaño al mismo tiempo
for animal,numero in zip(animales,numeros):
    print(f"recorriendo la conjunto 1:{numero}")
    print(f"recorriendo la conjunto 2:{animal}")
    
#esta formula te tira del primer numero que le das hasta el anteultimo
#si le pones un solo numero va de 0 a ese  numero que le tiraste
for num in range(5,10):
    print(num)
    
#forma ineficiente de recorrer una conjunto con su indice
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una conjunto con su indice
for num in enumerate(numeros):
    indice=num[0]
    valor=num[1]
    print(f"el indice es:{indice} y el valor es :{valor}")
    
#usando else
for numero in numeros:
    print(f"ejecutando el ultimo bucle,el valor actual{numero}")
else:
    print("el bucle termino")