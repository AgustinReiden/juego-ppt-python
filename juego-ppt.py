nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

puntosj1 = 0
puntosj2 = 0

while puntosj1 < 3 and puntosj2 < 3:
    jugador1 = input(f"¡Hola {nombre1}! ¿Que eliges? ¿Piedra, papel o tijera?: ").lower()
    jugador2 = input(f"¡Hola {nombre2}! ¿Que eliges? ¿Piedra, papel o tijera?: ").lower()

    condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijera" and jugador2 == "papel"

    if jugador1 == jugador2:
        print("Ha sido un empate, se repite el juego!")
    elif condicion1 or condicion2 or condicion3:
        print("Ha ganado:", nombre1)
        puntosj1 += 1
    else:
        print("Ha ganado:", nombre2)
        puntosj2 += 1
    print(f"Puntuación: {nombre1} {puntosj1} - {nombre2} {puntosj2}")

if puntosj1 == 3:
    print(f"¡Felicidades {nombre1}! Has ganado el juego ")
else:
    print(f"¡Felicidades {nombre2}! Has ganado el juego")