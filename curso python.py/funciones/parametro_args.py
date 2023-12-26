#forma no optima de sumar valores
#def suma(lista):
 #   numeros_sumados=0
 #   for numero in lista:
 #       numeros_sumados=numeros_sumados+numero
 #   return numeros_sumados
#resultado=suma([5,3,9,6])
#print(resultado)

#forma optima,utilizando el parametro args(*)
def suma(*numeros):
    return sum(numeros)

resultado=suma(5,3,7,9)
print(resultado)