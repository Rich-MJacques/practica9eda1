#esto es un comentario de una sola linea
'''
esto es un comentario de varias lineas
python es un programa que no genera archivo ejecutable, 
siempre necesitas python para ejecutar al programa, 
osea el interprete(python3)

'''
""" 
Esto es comentrario de varias lineas
"""
print("Hola Mundo")#no hay punto y coma
x=10
print(type(x))
print(x)
x=y=z=2.3
print(x,y,z)
print(type(x))
x="cadena"
print(x, type(x))

c1="hola"
c2 = "ricardo"
saludo = c1 + " "+c2#esto se llama concatenacion
print(saludo)
saludo2="{} {} {}".format(c1,c2,3)
print(saludo2)
saludo3= "cambio de orden {1} {2} {0}".format(c1,c2,3)
print(saludo3)
