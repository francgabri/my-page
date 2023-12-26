#abriendo el archivo con with open
with open("archivos\\texto de franco.txt",encoding="UTF-8") as archivo:
 #leemos el archivo
 contenido=archivo.read()
 #mostramos el archivo
print(contenido)
#no es necesario cerrar el archivo con with open