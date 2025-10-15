""" #importaciones, librerias
import random

sensorCarrito = random.randint(60,100)
sensorTemperatura =random.randint(18,35)

print("Sensor: ", sensorCarrito)
print("Temperatura: ",sensorTemperatura)

if sensorCarrito > 85 and sensorTemperatura < 28:
    print("Calidad mala del aire y temperatura optima")
else:
    print("Calidad buena, temperatura mala")
 """
#---------------------------------------------------------------------
""" #importaciones, librerias
import random

sensorMovimiento = True
sensorDistancias =random.randint(10,100)

print("Distancia: ",sensorDistancias)

if sensorDistancias == 0:
    print("Movimiento detectado")
elif sensorDistancias < 20:
    print("Frena")
elif sensorDistancias > 50:
    print("Acelera")
elif sensorDistancias > 90 and sensorDistancias <=100:
    print("Baja la velocidad, las multas estan caras") """

#--------------------------------------------------------------
tipo_de_pokemon = input("Ingresa el tipo de pokemon (agua, fuego, planta): ").lower()
print("Seleccionaeste el pokemon: ",tipo_de_pokemon)

#parte logica

if tipo_de_pokemon=="agua":
    print("Tu Pokemon es Squirtle")
elif tipo_de_pokemon=="fuego":
    print("Tu Pokemon es Charmander")
elif tipo_de_pokemon=="planta":
    print("Tu Pokemon es Bulbasaur")
else:
    print("Pokemon no valido, especie extinta")