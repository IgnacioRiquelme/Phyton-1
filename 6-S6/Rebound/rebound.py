numero = int(input("Ingresa un número: "))

if numero > 0:
    if numero % 2 == 0: input(f"El número {numero} es positivo y par.")
    else: input(f"El número {numero} es positivo e impar.")
elif numero < 0:
    if numero %2 == 0: input(f"El número {numero} es negativo y par.")
    else: 
        print(f"El número {numero} es negativo e impar.")
else:         
    print("El valor es 0.")