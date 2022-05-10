def saludo(): #definir la función
    print("hola mundo")
    print("Mision Tic 2022")
    
def suma(a,b): # a y b son los parámetros de la función
    print(a+b)

saludo() #llamar a la función  
x = int(input("digite num1: "))
y = int(input("digite num2: "))
suma(x,y) #x, yson los argumentos de la función

def resta(a,b):
    return a-b

print(resta(90,15))

