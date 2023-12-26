def frase(nombre,apellido,adjetivo):
 return f"hola {nombre} {apellido},como estas {adjetivo}?"

frase_resultante=frase("franco","mariño","capo")
print(frase_resultante)

#otra forma de hacerlo sin depender del orden de las palabras
def frase(nombre,apellido,adjetivo):
 return f"hola {nombre} {apellido},como estas {adjetivo}?"

frase_resultante=frase(adjetivo="capo",nombre="franco",apellido="mariño",)
print(frase_resultante)
