#Bucles

#esta instruccion ejecuta N veces una parte del codigo
#realice una plana repitiendo 100 la siguente frase

""" for i in range(100):
    print(f"Sopa de caracol: {i+1}") """


#realice un selector de numero pares de 1 hasta 2563
""" for i in range (0,100):
    if i % 2 == 0:
        print(i)

 """
#realice un programa que sume todos los numeros pares del 1 al 36
""" suma = 0
for i in range (1,36):
    if i % 2 == 0:
        suma += i
        print("La suma es: ",suma)
 """
#calculo media aritmetico o promedio.

CapturaEdad=0
suma=0
for i in range (1,22):
    CapturaEdad = int(input(f"Ingrese su promedio, usuario {i}:"))
    suma += CapturaEdad

    promedio = suma/21
print("Promedio general: ", promedio)