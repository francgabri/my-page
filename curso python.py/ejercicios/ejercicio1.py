#datos
curso_dalto=1.5
curso_minimo=2.5
crudroDalto=3.5
promedio=4
crudo2=5
curso_maximo=7

#diferencias de duracion 
diferencia_con_min=100-curso_dalto/curso_minimo*100
diferencia_con_max=100-(round(curso_dalto/curso_maximo*100,1))
diferencia_con_el_promedio=100-curso_dalto/promedio*100

#mostrando las diferencias de duracion (ejercicio A)
print(f"el curso de dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"el curso de dalto dura un {diferencia_con_max}% menos que el mas lento")
print(f"el curso de dalto dura un {diferencia_con_el_promedio}% menos que el promedio")

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio=100-(round(promedio/crudo2*100,1))
tiempo_vacio_dalto=100-(round(curso_dalto/crudroDalto*100,1))

print(f"el curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio" )
print(f"el curso de dalto elimino un {tiempo_vacio_dalto}% de tiempo vacio" )

#mostrando diferencias si los cursos duraran 10 horas
print(f"ver 10 horas de este curso equivale a ver {(round(promedio/curso_dalto*100,1))} horas de otros cursos")
print(f"ver 10 horas de otros cursos equivale a ver {(round(curso_dalto/promedio*100,1))} horas de este curso")

