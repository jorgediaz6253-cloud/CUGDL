""" #funciones
import math
def multiplicacion(a, b, c, d):
    print("La multiplicacion de a*b*C*d = ", a*b*c*d)

def division(a,b):
    print("la division es: ", a/b)

multiplicacion(2,2,2,2)
division(10,5)
"""
""" 
def area_circulo(radio):
    return 3.14 * radio**2 

#funcion para perimetro circulo
def perimetro_circulo(r):
    return 2*3.14*r
#print("el perimetro es el circulo: ", perimetro_circulo(1))

#funcion area triangulo
def area_triangulo(b,h):
    return (b*h)/2
#print("El area de un triangulo es: ", area_triangulo(3,4))

suma_areas=area_circulo(2.5) + area_triangulo(3,4)
print("La suma de areas es: ",suma_areas)

 """

#--------------------------------------------------------------------------------#
import random
import time

#funcion dado
def tirar_dado():
    return random.randint(1,6)

def tirar_dado2():
    return random.randint(1,6)

bandera=True

while bandera:
    selector=input("presione cualquier ecla para jugar o q para salir: ").lower()
    if selector == "q":
        bandera=False
    else:
        print("Tirando dado 1...")
        time.sleep(1)
        print("Tirando dado 2...")
        time.sleep(1)
        d1=tirar_dado()
        d2=tirar_dado2()
        print("resultado el dado: ", d1, d2, "=", d1+d2)