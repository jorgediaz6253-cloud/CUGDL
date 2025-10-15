#bucle loop
#Banco MALESTAR 2
import random
bandera = True

while bandera == True:

    print("Bienvenido a su banco MALESTAR")
    print("Seleccione su transaccion: ")
    print("1. Consultar saldo")
    print("2. Retiro de efectivo")
    print("3. Donaciones \n")

    seleccion = int(input("Ingrese la transaccion a realizar: "))
    saldo = random.randint(0,5000)

    if seleccion == 1:
        print("Su saldo es: ", saldo)
        otratransaccion= int(input("Desea realizar otra transaccion? 1.Si 2.No: "))
        if otratransaccion !=1:
            bandera = False

    elif seleccion == 2:
        print("Saldo anterior: ",saldo)
        retiro=int(input("Ingrese saldo a retirar: "))
        print("Saldo post retiro: ",(saldo - retiro))
        otratransaccion= int(input("Desea realizar otra transaccion? 1.Si 2.No: "))
        if otratransaccion !=1:
            bandera = False
    elif seleccion == 3:
        print("Funcion no disponible")
        otratransaccion= int(input("Desea realizar otra transaccion? 1.Si 2.No: "))
        if otratransaccion !=1:
            bandera = False
    else:
        print("Funcion no dispobible")
