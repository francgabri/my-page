cadena1="hola soy franco mariño"
cadena2="BIENVENIDO"
#print(dir(CADENA_1)) #El dir se usa para dar los atributos de lo que tenemos dentro

resultado=cadena1.upper()#el upper()se usa para pasar a mayuscula el string
resultado2=cadena2.lower()#el lower()se usa para pasar a minuscuas el string
resultado3=cadena1.capitalize() #el capitalize()se usa para que el primer letra este en mayuscula
busqueda_find=cadena2.find("h")#el find()te tira el numero de la posicion del objeto
#si no lo encuentra te devuelve -1
busqueda_index=cadena1.index("o")#es igual al find pero si no encuentra nada te tira error
#devuelve true si es numerico , si no lo es false
es_numerico=cadena1.isnumeric()
#si es alfanumerico te tira true,si no te tira false,el espacio no es alfanumerico
es_alfanumerico=cadena1.isalpha()
#cuenta coincidencias 
contar_coincidencias=cadena1.count("o")
#contamos cuantos caracteres tiene una cadena
contar_caracteres=len(cadena1)
#verificamos si una cadena empieza con otra cadena dada,si es asi devuelve true
empieza_con=cadena1.startswith("hola")
#verificamos si una cadena termina con otra cadena dada,si es asi devuelve true
termina_con=cadena1.endswith("mariño")
#reemplaza parte de una cadena dada por otra dada
cadena_nueva=cadena1.replace("la","lu")
#separar cadenas con la cadena que le pases
cadena_separada=cadena1.split(",")
print(cadena_separada)