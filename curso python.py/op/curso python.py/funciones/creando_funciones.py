#crear una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo=sexo.lower()
    if (sexo =="mujer"):
        adjetivo ="reina"
    elif(sexo =="hombre"):
        adjetivo="titan"
    else:
        adjetivo="amor"
        
    print(f"hola {nombre} ,mi {adjetivo}¿como andas?")
saludar("camila","mujer")
saludar("fran","hombre")
saludar("noa","no binario")
#crear una funcion que nos retorna valores
def crear_conntraseña_ramdon(num):
   chars="ahdwcnun"
   num_entero=str(num)
   num=int(num_entero[0])
   c1=num-2
   c2=num
   c3=num-5
   contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
   return contraseña

password=crear_conntraseña_ramdon(5)
frase=f"tu contraseña es:{password}"
print(frase)