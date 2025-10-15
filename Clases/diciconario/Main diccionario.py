from last_name import last_name
from names import names

#crear una funcion que fenere nombres completos utilizando los arreglos

import random
#tips todo esto de forma aleatoria

def aleatoria():
    return random.randint(0,999)

for i in range(100):
    print(names[aleatoria()], last_name[aleatoria()], last_name[aleatoria()])