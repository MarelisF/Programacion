##Ejercicio suelto No 4

##Entrada de la edad de Juan, ya que esta es vital para el desarrollo del ejercicio

edadJ= int(input("Edad de Juan "))
##Para la edad de Alberto segun el texto tenemos
edadA= int((edadJ*2)/3)
##Ahora Ana tiene 4/3 de la edad de Juan, entonces
edadAn= int((edadJ*4)/3)
##La edad de la madre es la suma de las tres edades
L= [edadJ,edadA,edadAn]
edadmadre= 0
##A continuación el siguiente for iterará en cada elemento de la lista creada con las edades para sumarlas
for i in L:
  edadmadre += i
print("Edad de Juan",edadJ,",","edad de Alberto", edadA, "edad de Ana",edadAn,"edad de la madre",edadmadre)