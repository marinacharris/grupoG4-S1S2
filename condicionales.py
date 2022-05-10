#Realice un programa que lea un numero entero y diga si es mayor o igual a 100
mensaje = "S" # = es un operador de asignación
while mensaje == "S": # == es un operador de relación o comparación
    respuesta = input("Digite el numero:\n")
    numero1 = int(respuesta)
    if numero1 >= 100:
        print(f"El número {numero1} es mayor o igual a 100")
    else:
        print(f"El número {numero1} es menor a 100")
    mensaje = input("Presione S para continuar o cualquier tecla para salir")