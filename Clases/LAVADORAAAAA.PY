#INICIO
import time
bandera = True
ciclo = 0
tiempo = 0
temperatura = 0

while bandera:
    print("Bienvenido al sistema de seleccion de lavado")
    print("Seleccione el tipo de ropa")
    print("1. Delicada")
    print("2. Normal")
    print("3. Muy sucia")
    seleccion=int(input("Seleccione el numero: "))

    if seleccion == 1:
        ciclo = "Lavado Suave"
        tiempo = 30
        temperatura = 30
    elif seleccion == 2:
        ciclo = "Lavado Normal"
        tiempo = 45
        temperatura = 40
    elif seleccion == 3:
        ciclo = "Lavado Intenso"
        tiempo = 60
        temperatura = 60
    else: 
        print("No valida")
    
    print("-------------------------------------------------------------------")
    print("CONFIGURACION SELECCIONADA")
    print("Ciclo: ", ciclo)
    print("Tiempo estimado: ", tiempo, "minutos")
    print("Temperatura: ", temperatura, "°C")
    
    sn=input("Desea iniciar lavado?: s/n: ").lower()
    if sn !="s":
        print("Lavado cancelado")
        bandera = False
    else:
        print("Iniciando lavado...")
        time.sleep(2)
        print("Lavado finalizado :D")
        print("-------------------------------------------------------------------")
    
"""     otrociclo= int(input("Desea realizar otro ciclo?: 1.Si 2.No = "))
    if otrociclo == 1:
        bandera = True
    else:
        bandera = False
        print("Gracias por usar nuestros serviciosssss :D")
 """
