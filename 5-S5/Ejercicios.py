"""
La resistencia dentro de un circuito paralelo se calcula como:
RT= 1/((1 /R1)+(1/R2)+(1/R3)+(1/Rn))
Donde:
● RT es la resistencia total.
● R1 es la resistencia 1.
● R2 es la resistencia 2.
● R3 es la resistencia 3.
● Rn la n-ésima resistencia.
Realizar el código en Python para calcular la resistencia total del circuito.
"""

r1 = float(input("Ingrese el valor de la resistencia 1: "))
r2 = float(input("Ingrese el valor de la resistencia 2: "))
r3 = float(input("Ingrese el valor de la resistencia 3: "))
rT = (1/((1 /r1)+(1/r2)+(1/r3)))
print("La resistancia total es: {:.3f}".format(rT))


print("------------------------------------------------------------------------------")

"""
Realizar el calculo de la hipotenusa requiriendo el ingreso del cateto a y cateto b por parte del usuario en consola
"""
import math
cateto_a = float(input("Ingrese el valor del cateto del triangulo: "))
cateto_b = float(input("Ingrese el valor del otro cateto del triangulo: "))
hipotenusa = math.sqrt(cateto_a**2 +cateto_b**2) 
print (f"la hipotenusa es {hipotenusa}")

print("------------------------------------------------------------------------------")

"""
Pedir el ingreso de dos textos al usuario por consola y comparar si son iguales o del mismo tamaño
"""
texto1 = input("Ingrese el primer texto: ")
texto2 = input("Ingrese el segundo texto: ")

if len(texto1) == len(texto2):
    if texto1 == texto2:
        print("Textos iguales y misma longitud")
    else:
        print("Textos diferentes misma longitud")
else:
    print("Textos diferentes")

"""
if len(texto1) == len(texto2):
    print("Textos del mismo tamaño")
elif texto1 == texto2:
    print("Textos iguales")
else:
    print("Textos diferentes")
"""


print("------------------------------------------------------------------------------")


"""
Simulación de una bomba de tiempo. Irá el tiempo desde el 5 al 1 en decremento. Al ejecutar el programa, se imprimirá el mensaje "Booom"
"""
import time
i = 5
while i >= 1:
    print(i)
    i -=1
    time.sleep(1)
print("Boom!!!")

print("------------------------------------------------------------------------------")

"""
Realizar la ejecución de un menú utilizando el lenguaje Python, donde se le indiquen varias opciones a seleccionar por el usuario y una opción para salir del menú.
Utilizar ciclos y estructuras condicionales.
"""
import re

opcion = ""
patron = re.compile("(?<!\\S)\\d(?!\\S)") #compilacion de patron
while opcion != "5":
    print("Hola, Bienvenido al menu")
    print("1.- Opción 1")
    print("2.- Opción 2")
    print("3.- Opción 3")
    print("4.- Opción 4")
    print("5.- Salir del menu")
    
    opcion = input() #leyendo la opcion
    if re.match(patron,opcion):
        if opcion == "1":
            print("Realizando la opcion 1")
        elif opcion == "2":
            print("Realizando la opcion 2")
        elif opcion == "3":
            print("Realizando la opcion 3")
        elif opcion == "4":
            print("Realizando la opcion 4")
        elif opcion == "5":
            print("Saliendo, hasta luego")
            #break
        else:
            print("Ingresaste una opcion invalida , favor ingresar nuevamente") 
    else:
        print("Ha ingresado una opcion incorrecta, valide el ingreso")                           
    
print("------------------------------------------------------------------------------")
    
while True:
    opcion = int(input("Hola, bienvenido\n "
                    "1.- Saludar\n "
                    "2.- preguntar que hay en la tele\n "
                    "3.- que opinas de la música que escucho?\n"
                    "4.- que estás sintiendo ahora?\n"
                    "5.- Salir\n\n"                
                    "Ingresa una opción => "))
    match opcion:
        case 1:
            print("Hola, que tal?")
        case 2:
            print("No hay nada bueno")
        case 3:
            print("Es buena música")
        case 4:
            print("Tengo hambre!")
        case 5:
            print("Nos vemos!")
            break
        case _:
            print("Esa opcion no es válida!")    
    