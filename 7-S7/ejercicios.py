nombres = ["Juan","Maria","Pedro","Ana","Roberto", "Lucia", "Luis"]

for i in nombres:
    if len(i) >= 5:
        print(i)

"""   Otra Forma
name = ["Juan", "Maria", "Pedro", "Ana", "Roberto", "Lucia", "Luisa"]
name_len_five = list(filter(lambda x: len(x) >= 5, name))
print(name_len_five)
"""

print("--------------------------------------------------------------")


""" 

"""

lista = ["gato","perro","elefante","jirafa","tigre"]

longitudes = []
for i in range(len(lista)):
    longitudes.append(len(lista[i]))
    
print(longitudes)   

""" 

""" 


for i in lista :
    longitudes.append(len(i))

print(longitudes)


print("--------------------------------------------------------------")


""" 
Solicita al usuario ingresar una contraseña hasta que la contraseña ingresada coincida con una contraseña predefinida
"""

password = "pass123"
"""
while True:
    clave = input("Ingresa la clave: ")
    if password == clave:
        print("Clave correcta")
        break
    else:
        print("Contraseña incorrecta, ingrese nuevamente: ")
"""       
print("Solo tiene 3 intentos")
intentos = 1

while intentos <= 3:
    clave = input("Ingresa la clave: ")
    if password == clave:
        print("Clave correcta")
        intentos = 4
    elif intentos == 3:
        print("Cantidad de intentos completada")
        intentos = 4
    else:
        print("Intento {intentos} de 3, contraseña incorrecta ingrese nuevamente: ")       

print("--------------------------------------------------------------")

