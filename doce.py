##Ejercicio propuesto No 12
##Se desea saber cuál es el salario bruto, la retención en la fuente y el salario neto del trabajador.
##Para ello se le pide al usuario ingresar sus horas trabajadas
horas = float(input("Ingrese el numero de horas trabajadas "))
##Luego el valor de su sueldo por hora
salario = float(input("Ingrese el valor de su salario por hora "))
##Luego llamaremos porcentajeretiene al porcentaje de retencion del sueldo
porcentajeretiene = 0.125
##Así llegamos a que el salario bruto es lo que pagan por hora, multiplicado por el numero de horas
salariobruto = salario*horas
##El valor de la retención es el salario bruto por el porcentaje que retiene
retencion = salariobruto*porcentajeretiene
##Finalmente, se tiene el salario neto que es la resta entre el salario bruto y su retención
salarioneto = salariobruto-retencion
print("El valor de su salario bruto es de",salariobruto, "pesos")
print("El valor de su retencion en la fuente es de",retencion, "pesos")
print("El valor de su salario neto es de",salarioneto, "pesos")
