import random

def juego():
    opciones = ["piedra", "papel", "tijera"]
    print("¡Bienvenido a Piedra, Papel o Tijera!")
    print("Opciones: piedra, papel o tijera")

    usuario = input("Elige tu opción: ").lower()
    while usuario not in opciones:
        usuario = input("Opción inválida, intenta de nuevo (piedra, papel, tijera): ").lower()

    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste! 🎉")
    else:
        print("Perdiste 😢")

# Ejecutar el juego
juego()