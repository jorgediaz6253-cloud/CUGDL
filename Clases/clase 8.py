#Realizar un programa de piedra papel o tijera.

import random
bandera = True

while bandera:
    print("Bienvenido a piedra, papel o tijera")
    maquina=random.randint(1,3)
    seleccion=int(input("Selecciona 1.piedra, 2.papel, 3.tijera, 4.salir:  "))
    print("-------------------------------------")
    if seleccion == 4:
        bandera = False
    elif seleccion ==  maquina:
        print("Empate")
    elif seleccion == 1 and maquina == 3:
        print("Ganaste con tijera")
    elif seleccion == 2 and maquina == 1:
        print("Ganaste contra piedra")
    elif seleccion == 3 and maquina == 2:
        print("Ganaste contra papel")
    else:
        print("Perdiste!!")