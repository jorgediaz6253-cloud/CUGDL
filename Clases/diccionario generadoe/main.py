#crear una funcion que genere un codigo aleatorio siguiendo la noomenclatura de la UDG
#costa de 9 numeros
#debe retonrnar en el tipo string
#2 ----
 
#crear una funcion que genere un diccionario siguiendo, el formato a continuacion y rellenando los datos
from last_name import last_name
from names import names
import random
#instruccion 1

def generadorCodigo():
    return f"225{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
    
def aleatorio():
    return random.randint(0,999)

def generadorDiccionario():
    return{
        "codigo": generadorCodigo(),
        "nombre":(names[aleatorio()]),
        "apellido_p":(last_name[aleatorio()]),
        "apellido_m":(last_name[aleatorio()])
    }
for i in range (5):
    print(generadorDiccionario())
