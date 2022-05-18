import random
import PySimpleGUI as sg

valores = 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
palo = 'Diamante', 'Corazones', 'Pica', 'Trébol'

texto_figura = ''
texto_resultado = ''
texto_mismo_palo = ''

# Esta tupla nos servirá para luego asignar un nombre a las cartas con valor 10.
figuras = 10, 'J', 'Q', 'K'

# Inicialización de las variables de los puntos de cada jugador.
puntos_jugador, puntos_crupier = 0, 0

# Mano del jugador
c1_jugador = random.choice(valores), random.choice(palo)
c2_jugador = random.choice(valores), random.choice(palo)

c3_jugador = 0, '.', 'No pidió tercera carta'

# Mano del crupier
c1_crupier = random.choice(valores), random.choice(palo)
c2_crupier = random.choice(valores), random.choice(palo)

c3_crupier = 0, '.', 'No pidió tercera carta'

# Le asignamos nombres a las cartas
if c1_jugador[0] == 10:
    # Si el valor de la carta es 10, le asignamos al azar una figura
    c1_jugador = c1_jugador[0], c1_jugador[1], random.choice(figuras)
elif c1_jugador[0] == 11:
    # Si el valor de la carta es 11, entonces le asignamos el nombre as
    c1_jugador = c1_jugador[0], c1_jugador[1], 'As'
else:
    # Si tiene otro valor, le asignamos de nombre un str que contiene el valor de la carta
    c1_jugador = c1_jugador[0], c1_jugador[1], str(c1_jugador[0])

if c2_jugador[0] == 10:
    c2_jugador = c2_jugador[0], c2_jugador[1], random.choice(figuras)
elif c2_jugador[0] == 11:
    c2_jugador = c2_jugador[0], c2_jugador[1], 'As'
else:
    c2_jugador = c2_jugador[0], c2_jugador[1], str(c2_jugador[0])

if c1_crupier[0] == 10:
    c1_crupier = c1_crupier[0], c1_crupier[1], random.choice(figuras)
elif c1_crupier[0] == 11:
    c1_crupier = c1_crupier[0], c1_crupier[1], 'As'
else:
    c1_crupier = c1_crupier[0], c1_crupier[1], str(c1_crupier[0])

if c2_crupier[0] == 10:
    c2_crupier = c2_crupier[0], c2_crupier[1], random.choice(figuras)
elif c2_crupier[0] == 11:
    c2_crupier = c2_crupier[0], c2_crupier[1], 'As'
else:
    c2_crupier = c2_crupier[0], c2_crupier[1], str(c2_crupier[0])

# Determinamos los puntos del jugador:
if c1_jugador[0] + c2_jugador[0] >= 17:
    # Si sus primeras dos cartas suman más de 17 puntos, el jugador no pide más cartas
    puntos_jugador = c1_jugador[0] + c2_jugador[0]
else:
    # Si suman menos de 17, el jugador pide su tercera carta y se calcula el puntaje
    c3_jugador = random.choice(valores), random.choice(palo)

    if c3_jugador[0] == 10:
        c3_jugador = c3_jugador[0], c3_jugador[1], random.choice(figuras)
    elif c3_jugador[0] == 11:
        c3_jugador = c3_jugador[0], c3_jugador[1], 'As'
    else:
        c3_jugador = c3_jugador[0], c3_jugador[1], str(c3_jugador[0])

    puntos_jugador = c1_jugador[0] + c2_jugador[0] + c3_jugador[0]

    if puntos_jugador > 21:
        # Si el jugador tiene más de 21 puntos, analizamos si alguna de las cartas es un as y reemplazamos su valor
        # por 1
        if c1_jugador[0] == 11:
            c1_jugador = 1, c1_jugador[1], 'As'
        elif c2_jugador[0] == 11:
            c2_jugador = 1, c2_jugador[1], 'As'
        elif c3_jugador[0] == 11:
            c3_jugador = 1, c3_jugador[1], 'As'
        puntos_jugador = c1_jugador[0] + c2_jugador[0] + c3_jugador[0]

if c1_crupier[0] + c2_crupier[0] >= 17:
    # Si sus primeras dos cartas suman más de 17 puntos, el crupier no pide más cartas
    puntos_crupier = c1_crupier[0] + c2_crupier[0]
else:
    # Si suman menos de 17, el crupier pide su tercera carta y se calcula el puntaje
    c3_crupier = random.choice(valores), random.choice(palo)
    if c3_crupier[0] == 10:
        c3_crupier = c3_crupier[0], c3_crupier[1], random.choice(figuras)
    elif c3_crupier[0] == 11:
        c3_crupier = c3_crupier[0], c3_crupier[1], 'As'
    else:
        c3_crupier = c3_crupier[0], c3_crupier[1], str(c3_crupier[0])

    puntos_crupier = c1_crupier[0] + c2_crupier[0] + c3_crupier[0]

    if puntos_crupier > 21:
        # Si el crupier tiene más de 21 puntos, analizamos si alguna de las cartas es un as y reemplazamos su valor
        # por 1
        if c1_crupier[0] == 11:
            c1_crupier = 1, c1_crupier[1], 'As'
        elif c2_crupier[0] == 11:
            c2_crupier = 1, c2_crupier[1], 'As'
        elif c3_crupier[0] == 11:
            c3_crupier = 1, c3_crupier[1], 'As'
        puntos_crupier = c1_crupier[0] + c2_crupier[0] + c3_crupier[0]

# Determinamos si alguno de los dos se pasó de 21, si lo hizo, su puntaje se vuelve 0
if puntos_jugador > 21:
    puntos_jugador = 0
if puntos_crupier > 21:
    puntos_crupier = 0

# Determinamos quien gano:
if puntos_jugador > puntos_crupier:
    texto_resultado = 'Gano el jugador con: ' + str(puntos_jugador) + ' puntos frente a: ' + str(puntos_crupier) + \
                      ' puntos del crupier.'
elif puntos_jugador < puntos_crupier:
    texto_resultado = 'Gano el crupier con: ' + str(puntos_crupier) + ' puntos frente a: ' + str(puntos_jugador) + \
                      ' puntos del jugador.'
else:
    texto_resultado = 'Empate! Tanto jugador como crupier tienen ' + str(puntos_jugador) + ' puntos.'

# Determinamos si el palo y el número de las primeras cartas de ambos coinciden:
mismo_palo = c1_jugador[1] == c1_crupier[1]
if mismo_palo:
    # Si coinciden, verificamos si tienen el mismo valor
    mismo_valor = c1_jugador[0] == c1_crupier[0]

    if mismo_valor:
        # Si además tienen el mismo valor, mostramos un mensaje especial (recibieron la misma carta)
        texto_mismo_palo = 'Las primeras cartas de ambos jugadores son iguales (mismo palo y valor).'
    else:
        # En caso de que solo compartan palo, mostramos un mensaje que lo diga.
        texto_mismo_palo = 'Las primeras cartas de ambos jugadores tienen el mismo palo.'

# Determinamos si salio alguna figura:
figura_jugador = (c1_jugador[2] == 'J' or c1_jugador[2] == 'Q' or c1_jugador[2] == 'K' or
                  c2_jugador[2] == 'J' or c2_jugador[2] == 'Q' or c2_jugador[2] == 'K' or
                  c3_jugador[2] == 'J' or c3_jugador[2] == 'Q' or c3_jugador[2] == 'K')

figura_crupier = (c1_crupier[2] == 'J' or c1_crupier[2] == 'Q' or c1_crupier[2] == 'K' or
                  c2_crupier[2] == 'J' or c2_crupier[2] == 'Q' or c2_crupier[2] == 'K' or
                  c3_crupier[2] == 'J' or c3_crupier[2] == 'Q' or c3_crupier[2] == 'K')

figura = figura_crupier or figura_jugador

if figura:
    texto_figura = 'Salió al menos una figura en la ronda.'
else:
    texto_figura = 'En esta ronda, no salio ninguna figura.'

# Lanzamos un popup de PySimpleGUI para mostrar la información de manera más visual.
sg.popup(f'La mano del jugador es: \n\n'
         f' * {str(c1_jugador[2])} de {str(c1_jugador[1])}, valor: {str(c1_jugador[0])}\n'
         f' * {str(c2_jugador[2])} de {str(c2_jugador[1])}, valor: {str(c2_jugador[0])}\n'
         f' * {str(c3_jugador[2])} de {str(c3_jugador[1])}, valor: {str(c3_jugador[0])}\n\n'
         f'La mano del crupier es: \n\n'
         f' * {str(c1_crupier[2])} de {str(c1_crupier[1])}, valor: {str(c1_crupier[0])}\n'
         f' * {str(c2_crupier[2])} de {str(c2_crupier[1])}, valor: {str(c2_crupier[0])}\n'
         f' * {str(c3_crupier[2])} de {str(c3_crupier[1])}, valor: {str(c3_crupier[0])}\n\n'
         f'{texto_resultado}\n'
         f'{texto_figura}\n'
         f'{texto_mismo_palo}\n', title='TP1: BlackJack')
