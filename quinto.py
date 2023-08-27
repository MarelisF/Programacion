##Ejercicio suelto No 5
##Hallar el valor de la suma ( es el ejercicio resuelto)
##Comenzamos con un acumulador en cero al cual se le irán sumando algunos valores
suma = 0
##X es el numero que el usuario ingresa para empezar el proceso
x = int(input("Ingrese el valor donde quiere que inicie la suma " ))
# En la siguente linea se sumará el valor ingresado
suma += x
##Luego se ingresa el x2, será un valor que se elevará al cuadrado y se sumará con el x ya ingresado
x2 = int(input("Ingrese el segundo valor que se elevará al cuadrado "))
x = x+x2**2
suma = suma+x/x2
print("el valor de la suma es",suma)