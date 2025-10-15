
#fatima salazaar
#jorge diaz abarca

from collections import deque
import time

BANDERA= True
estacionamiento = deque(["A1", "B1","C1","D1", "E1","F1"])
limite = 10

while BANDERA:
    print("ESTACIONAMIENTO CUGDL")
    print("-------------------------")
    print("1.INGRESAR AUTO")
    print("2. RETIRAR AUTO")
    print("3. MOSTRAR AUTOS")
    print("4. SALIR")
    opcion=int(input(""))

    if opcion == 1:
        if  len(estacionamiento) >=limite:
            print("CAPACIDAD MAxIMA")
        else:
            carro = input("Ingrese nombre del auto: ")
            estacionamiento.append(carro)
            print("Su auto se agrego exitosamente")
            print("Autos en estacionamiento", estacionamiento)
    elif opcion == 2:
        if estacionamiento:
            salida = estacionamiento.popleft()
            print("El carro que salio fue: ", salida)
            print("Autos en estacionamiento: ", estacionamiento)
        else:
            print("No hay autos por retirar")
    elif opcion == 3:
        print("Autos en estacionamiento",estacionamiento)
    else:
        BANDERA=False
        print("Bye.")

