##Ejercicio propuesto No 17
##Para este ejercicio lo primero que necesitamos es que nos den el radio para ello
import math
radio= int(input("Ingrese el radio del circulo "))
##Como se necesita el numero pi para calcular el área se importa math
## A es el área, entonces
A = math.pi*(radio**2)
##Para la longitud de la circunferencia necesitamos el diámetro y el valor pi
l = math.pi*(radio*2)
## Por si desean el área y circunferencia redondeadas a 2 cifras decimales
A1 = round(A, 2)
l2 = round(l, 2)
print("El area del circulo redondeada es",A1)
print("La longitud de la circunferencia redondeada es",l2)
print("El area del circulo sin redondeaer es",A)
print("La longitud de la circunferencia sin redondear es",l)