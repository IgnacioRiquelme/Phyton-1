import random

palabras_secretas = ["arroz", "pollo", "pure", "choclo", "chorrillana"]
adivinar = random.choice(palabras_secretas)
# print(adivinar)
intentos = 5
turno = 0
ingreso = ""

while adivinar != ingreso and turno < intentos:
    ingreso = input("ingrese la palabra: ")
    turno += 1
    if ingreso == adivinar:
        print(f"Ha encontrado la palabra secreta en el intento numero {turno} ")
    elif turno == intentos:
        print (f"No tiene mas intentos, la palabra secreta era: {adivinar}")
    else:
        print(f"Fallaste, vas en el intento {turno} de 5")