import random

# Generar el mazo del dealer con tuplas (valor, palo)
def generar_mazo():
    return [(valor, palo) for valor, _ in [(str(v), v) for v in range(2, 11)] + [('A', 11), ('J', 10), ('Q', 10), ('K', 10)]
	for palo in ['Corazones', 'Diamantes', 'Tréboles', 'Picas']]

# Calcular el valor de una mano
def valor_mano(mano):
	#  Sumar los valores de cada carta, haciendo uso de recursividad para sumar sus elementos y si es k
    print(mano)
    return 0 if not mano else int(mano[0][0]) if mano[0][0].isdigit() else mano[0][1] + valor_mano(mano[1:])

# Pedir una carta del mazo
def pedir_carta(mazo):
    return (None, mazo) if not mazo else (mazo[0], mazo[1:])

# Función recursiva para jugar
def jugar(mazo_dealer, jugador1, jugador2):
    # Caso de finalización cuando alguien gana o pierde
    if valor_mano(jugador1) > 21:
        return "Jugador 1 se pasó. Jugador 2 gana."
    if valor_mano(jugador2) > 21:
        return "Jugador 2 se pasó. Jugador 1 gana."
    if valor_mano(jugador1) == 21:
        return "Jugador 1 tiene 21. Jugador 1 gana."
    if valor_mano(jugador2) == 21:
        return "Jugador 2 tiene 21. Jugador 2 gana."
    if not mazo_dealer:
        return f"Empate. Jugador 1: {valor_mano(jugador1)}, Jugador 2: {valor_mano(jugador2)}"
    
    # Repartir carta a uno de los jugadores
    carta, mazo_restante = pedir_carta(mazo_dealer)
    
    # Decidir recursivamente a quién darle la carta
    if input(""):
        return jugar(mazo_restante, jugador1 + [carta], jugador2)
    else:
        return jugar(mazo_restante, jugador1, jugador2 + [carta])

# Iniciar el juego
print(jugar(random.sample(generar_mazo(), k=52), [], []))