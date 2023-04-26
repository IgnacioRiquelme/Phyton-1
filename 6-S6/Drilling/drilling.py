num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))  
num_3 = int(input("Ingrese el tercer numero: "))

if len(set({num_1,num_2,num_3})) !=3:
    print("Debe ingresar numeros diferentes")
else:
    ordenados = sorted([num_1,num_2,num_3], reverse=True) 
    print(ordenados)   
