#importamos el modulo
import modulo_saludar
saludo=modulo_saludar.saludar("raul")

#otra forma de hacerlo (el as nos sirve para renombrar cosas)
from modulo_saludar import saludar,saludar_raro as saludar_como_coscu
saludo=saludar("agus")
saludo_r=saludar_como_coscu("fran")
#mostramos los resultados
print(saludo_r)
