#esto
multiplicar_por_dos=lambda x:x*2

#es lo mismo que esto(pero mas facil)
def multiplicar_por_dos(x):
    return x*2

#creando una funcion que diga si es par o no
numeros=[1,2,3,4,5,6,7,8,9]
#def es_par(num):
#    if (num%2==0):
#        return True
    
#usamos filter con una funcion comun
#numeros_pares=filter(es_par,numeros)
#ahora hacemos lo mismo que antes pero con lambda(MUCHO MAS EFICIENTE)
numeros_pares=filter(lambda numero:numero%2==0,numeros)
print(list(numeros_pares))