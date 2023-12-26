#la lista se puede madificar como ves aca
lista=["franco mariño","fisymath science",1.86,True]
lista[3]="cracken"
print(lista[3])

#mientras que la tupla no se puede modificar
tupla=("franco mariño","fisymath science",1.86,True)
#tupla[3]=picha  no va
print(tupla[3])

#creando un conjunto (set)
conjunto={"franco mariño","fisymath science",1.86,True,1.86}
#no te permite repetir datos ni buscarlos por indice,tiene los datos desordenados
print(conjunto)

#creando un diccionario,estructura (key:value y agregamos comas)
diccionario={
'nombre':"franco",
'edad': 20,
'emocionado_por_programar': True,
'dato_duplicado': "franco",
}

print(diccionario['emocionado_por_programar'])