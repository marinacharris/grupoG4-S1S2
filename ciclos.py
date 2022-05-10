#Realice un contador de 1 a 10
#ciclo while
contador = 1
while contador<=10:
    print(contador)
    contador +=1 #contador = contador + 1
print("fin del ciclo while")

contador = 0  # 1. siempre hay que inicializar la variable
while contador<10: # 2. Formular adecuadamente la condición
    contador = contador + 1 # 3. Modificar la variable
    print(contador) 
print("fin del ciclo while")

for cont in range(10): #cuenta de 0-9 o 0-(10-1)
    print(cont)
print("fin conteo")

for cont in range(1,11): #cuenta de 1-10, cuenta de uno en uno
    print(cont)
print("fin conteo")

for cont in range(0,26,5): # cuenta desde 0 hasta 25 de cinco en cinco
    print(cont)
print("cuanta en reversa")    
for cont in range(20,-1,-1):
    print(cont)

    