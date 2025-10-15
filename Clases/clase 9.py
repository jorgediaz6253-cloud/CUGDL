#Arreglos

Jericallo=["Tabata", "Dante", "Jorge", "Kitzia", "Leonardo", "Jillean", "Elena", "Ruben", "Atziry", "Marco", "Alex"]
TortaAhogada=["Perña", "Martha", "Tabata", "Ariel", "Miguel", "Jennifer", "Estela", "Raul", "Luis"]

""" print(TortaAhogada)
#agregar 
TortaAhogada.append("Diego")
print(TortaAhogada) """

#clear
""" print(Jericallo)
Jericallo.clear()
print(Jericallo) """

#copy
#CarneSuJuego = Jericallo.copy()

#Metodo extend
""" print("Antes de",Jericallo)
Jericallo.extend(TortaAhogada)
print("Despues de",Jericallo) """

#metodo count
""" Jericallo.extend(TortaAhogada)
print(Jericallo)
print(Jericallo.count("Tabata")) """

#index
Tapatios = Jericallo + TortaAhogada
""" print(Jericallo)
print(Tapatios.index("Jennifer"))
 """
#insert
""" print(Tapatios)
Tapatios.insert(7, "Paola")
print(Tapatios)
 """
#pop
""" print(Tapatios)
Tapatios.insert(12, "ProfeNava")
print(Tapatios)

Tapatios.pop(12)
Tapatios.pop(4)
Tapatios.pop(8)

print("Tapatios vaporizados: ",Tapatios) """
#remove
""" print(Tapatios)
Tapatios.remove("Miguel")
print(Tapatios) """

#reversa()
""" print(Tapatios)
Tapatios.reverse
print("reversa:", Tapatios) """

#bonussssss
#split, permite convertir o fraccionar un string en un arreglo
LoremIpsum="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
ArrayLIFromSting=LoremIpsum.split()
print(ArrayLIFromSting)

#metodo join
#el inverso del metodo join
StringLIFromArray= "2455".join(ArrayLIFromSting)
print(StringLIFromArray)

StringLIFromArray = StringLIFromArray.split("2455")
print(StringLIFromArray)