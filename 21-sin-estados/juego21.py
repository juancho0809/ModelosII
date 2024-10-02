import random

# Generar el mazo del dealer con tuplas (valor, palo)
def generar_mazo():
    return [(valor, palo) for valor in [(str(v), v) for v in range(2, 11)] + [('A', 11), ('J', 10), ('Q', 10), ('K', 10)]
	for palo in ['Corazones', 'Diamantes', 'Tréboles', 'Picas']]

def repartir_cartas(mazo, mano_jugador, mano_casa):

    random.shuffle(mazo) # La casa revuelve las cartas
    for _ in range(2):
        # Repartimos a la mano 1
        if mazo:  # Comprobar si quedan cartas en el mazo

            mano_jugador.append(mazo.pop(random.randint(0, len(mazo) - 1)))  # Retorna una carta a la baraja jugador
        
        # Repartimos a la mano 2
        if mazo:  # Comprobar si quedan cartas en el mazo
            
            mano_casa.append(mazo.pop(random.randint(0, len(mazo) - 1)))  # Retorna una carta a la baraja casa

    return mazo, mano_jugador, mano_casa


# Calcular el valor de una mano
def abs_valor_mano(mano):
	#  Sumar los valores de cada carta, haciendo uso de recursividad para sumar sus elementos si no es nula la lista
    
    return 0 if not mano else mano[0][0][1] + abs_valor_mano(mano[1:])

def contar_as(mano):
    if not mano:
        return 0 # Si en la iteracion es vacia se rompe

    if mano[0][0][0] == 'A': # Evalua la primera de esta iteracion
        return 1 + contar_as(mano[1:])
    else:
        return contar_as(mano[1:])

# Función para restar 10 a cada as que haga que se pase de 21, pero deja el mayor valor posible
def ajustar_valor(suma, ases):
    # Si el total es superior a 21 y hay ases que se pueden ajustar, reducir el total recursivamente.
    if suma > 21 and ases > 0:
        return ajustar_valor(suma - 10, ases - 1)
    return suma

# Funcion para dar el valor de la mano ajustado
def valor_mano(mano):
    return ajustar_valor(abs_valor_mano(mano), contar_as(mano))

# Función recursiva para jugar
def jugar(mazo, mano_jugador, mano_casa):
    # Diálogo de cada turno
    print("********************")
    print("Casa: ", mano_casa[0], ", **Oculta**")
    print("Tú: ", mano_jugador)
    print("********************")

    if valor_mano(mano_jugador) > 21:
        return "Perdiste! Te pasaste de 21 con " + str(valor_mano(mano_jugador))

    if input("La suma de tus cartas es " + str(valor_mano(mano_jugador)) +
             ", escribe según opción:\nTomar carta(t)\nQuedarse(q)\n").lower() == "t":
        if mazo:
            mano_jugador.append(mazo.pop(0)) # Tomar primer carta del mazo si no esta vacio
            print("Carta obtenida: ", mano_jugador[len(mano_jugador) - 1])
        
        return jugar(mazo, mano_jugador, mano_casa)
    
    else:
        print("********************")
        print("Juego de la casa")
        print("Mano inicial casa: ", mano_casa)
        print("Suma: ", valor_mano(mano_casa))
        while valor_mano(mano_casa) < valor_mano(mano_jugador):
            if mazo:
                mano_casa.append(mazo.pop(0)) # Tomar primer carta del mazo si no esta vacio
                print("Nueva mano: ", mano_casa)
                print("Suma: ", valor_mano(mano_casa))
        if valor_mano(mano_casa) > 21 or valor_mano(mano_casa) < valor_mano(mano_jugador):
            return "---- GANASTE!!! ----"
        else: 
            return "--- Ganó la casa ---"

# Implementar función jugar e imprimir resultado
print(jugar(*repartir_cartas(generar_mazo(),[],[])))