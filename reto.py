def CDT(usuario:str,capital:int,tiempo:int):
    intereses = (capital*0.03*tiempo)/12
    
    return f'Hola este es un mensaje de prueba y estos son los intereses {intereses}'
    
    
print(CDT("AB1012",1000000,3))
    