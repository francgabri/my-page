#creando una funcion que nos devuelva numeros primos
#entre 0 y el argumento que pasamos
def es_primo(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos=[]
    for i in range(3,num+1):
        resultado=es_primo(i)
        if resultado==True: primos.append(i)
    return primos
            
resultado=primos_hasta(100)
print()
#creando una funcion que muestre la serie de fibonacci entre el 0 hasta el numero dado
def fibonacci(num):
    a,b = 0,1
    fibonacci_lista=[]
    for i in range(num):
        if b > num:return fibonacci_lista
        else:
          fibonacci_lista.append(b)  
          a,b= b,a+b

resultado=fibonacci(21)
print(resultado)