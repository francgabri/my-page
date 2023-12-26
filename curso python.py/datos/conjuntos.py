#creamos un conjunto con set()
conjunto=set(["dato1","dato2"])
#metiendo un conjunto dentro de otro conjunto
conjunto1=frozenset(["dato1","dato2"])
conjunto2={conjunto1,"dato3"}
print(conjunto2)

#teoria de conjuntos
conjunto3={1,3,5,7}
conjunto4={1,3,7}
#verificando si es un subconjunto
resultado=conjunto4.issubset(conjunto3)
resultado=conjunto4<=conjunto3
#verificando si es un super conjunto
resultado=conjunto4.issuperset(conjunto3)
resultado=conjunto4>conjunto3
#verificar si hay algun numero en comun(cuando hay un numero igual ya es falso)
resultado=conjunto4.isdisjoint(conjunto3)
print(resultado)
