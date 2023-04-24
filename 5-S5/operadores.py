#operadores logicos
#and or not
#evaluar bool o booleanos True or False
a = True
b = False

print(a and b) # False,deben cumplirse las dos condiciones
print(a or b) # True, debe cumplirse alguna de las condiciones
print(not a) # False, not cambia el valor de la condicion
print(not (a or b)) # False
print(not (a and b)) # True
print("---------------------------------------------------------------")

# Operadores de comparacion
# Comparacion de numeros , tamaños,verificar contadores o itereadores
c = 10
d = 5

print(c < d) # False , Menor que
print(c > d) # True , Mayot que
#print(a > b) # True
#print(a < b) # False
print(c <= d) # False, Menor igual que
print(c >= d) # True, mayor igual que
print(c == d) # False, igual que
print(c != d) # True, distinto que