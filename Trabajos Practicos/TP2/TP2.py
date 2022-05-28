import random

# Constantes necesarias para generar cada carta
VALORES = 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
PALOS = 'Diamante', 'Corazones', 'Pica', 'Trébol'
FIGURAS = 10, 'J', 'Q', 'K'


def separador(n, salto):
    """Separa diferentes segmentos de la interfaz"""
    if salto:
        print('\n')
    print('-' * n)


def dar_carta(mano, valores, palos, figuras, puntos):
    """Toma los datos actuales de la mano del jugador o del crupier y los retorna actualizados habiéndoseles sumado una
    carta.
    """
    nueva_mano = mano
    carta = random.choice(valores), random.choice(palos)

    # Si la carta vale 10, se le asigna una figura
    if carta[0] == 10:
        carta = carta[0], carta[1], random.choice(figuras)
    # Si la carta tiene valor 11, se indica que es un As
    elif carta[0] == 11:

        # Si el puntaje se excediera de 21, el As adopta automáticamente un valor de 1
        if puntos + 11 > 21:
            carta = 1, carta[1], 'As'
        else:
            carta = carta[0], carta[1], 'As'
    else:
        carta = carta[0], carta[1], str(carta[0])

    # Se actualizan el puntaje y la mano
    puntos_actualizados = puntos + carta[0]
    nueva_mano += carta,

    # Si el puntaje supera los 21 puntos, busca entre las cartas de la mano si alguna es un As y cambiamos su valor
    if puntos_actualizados > 21:
        mano_control_as = ()
        puntos_actualizados = 0

        for carta in nueva_mano:
            nueva_carta = ()

            if carta[0] == 11:
                nueva_carta += (1, carta[1], carta[2])
                mano_control_as += nueva_carta,
                puntos_actualizados += nueva_carta[0]
            else:
                mano_control_as += carta,
                puntos_actualizados += carta[0]

        return mano_control_as, puntos_actualizados
    return nueva_mano, puntos_actualizados


def mostrar_opciones():
    """Muestra el menu de opciones y retorna la opcion escogida por el usuario."""
    print('Bienvenido al juego de BlackJack 2.0!')
    print('¿Que desea hacer?')
    print('[1] Apostar')
    print('[2] Jugar una mano')
    print('[3] Salir')

    opcion = 0
    while opcion <= 0 or opcion >= 4:
        opcion = int(input('Respuesta: '))
        separador(20, True)
        if 0 >= opcion >= 4:
            print('Por favor ingrese una opcion valida (1, 2 o 3)')

    return opcion


def mostrar_cartas(cartas, jugador):
    """Muestra la mano del jugador o del crupier."""
    print(f'Mano del {jugador}:')
    for carta in cartas:
        print(f'{carta[2]} de {carta[1]} con un valor de {carta[0]}')


def menu(nombre_jugador, monto):
    """Cuerpo del programa, aquí se recibe la opcion del usuario y se ejecuta la alternativa correspondiente a esa
    opcion.
    """

    # Variables que vamos a necesitar para las salidas
    acumulado = monto
    victorias = derrotas = racha_mas_larga = racha_actual = manos_bj_natural = cant_apuestas = total_apuestas = \
        mayor_perdida = 0
    monto_max = acumulado

    # Se muestran las ociones del menu
    opcion = mostrar_opciones()

    # Se ejecutará siempre mientras el usuario no ingrese la opcion de salir del juego
    while True:

        # Opción 1 (apuesta)
        if opcion == 1:
            apuesta = 0
            # Se controla que la apuesta cumpla con la condición requerida (0 < apuesta < 100000)
            while apuesta + acumulado > 100_000 or apuesta <= 0:
                apuesta = int(input('Ingrese la nueva apuesta: '))

                if apuesta + acumulado > 100_000:
                    print('La apuesta ingresada no es valida porque al monto acumulado sobrepasa el limite (100000)'
                          f'Por favor ingrese una apuesta menor a {100_000 - acumulado}.')
                elif apuesta <= 0:
                    print('La apuesta ingresada no es valida, por favor ingrese una apuesta mayor que cero.')

            # Se actualiza y muestra el acumulado.
            acumulado += apuesta
            print(f'Su nuevo monto acumulado es de: {acumulado}')

        # Opción 2 del programa, es el desarrollo del juego en sí.
        elif opcion == 2:
            # Variables necesarias para las salidas.
            cant_apuestas += 1
            puntos_jugador, puntos_crupier, monto_a_jugar = 0, 0, 0
            monto_inicial = acumulado
            bj_natural = bj_natural_crupier = False

            # Se define el monto apostado de esta ronda
            while monto_a_jugar <= 0 or monto_a_jugar > acumulado or monto_a_jugar % 5 != 0:
                monto_a_jugar = int(input('Su apuesta esta ronda (0 para salir al menú): '))
                separador(20, False)
                if monto_a_jugar > acumulado:
                    print('No dispone de esa cantidad.')
                elif monto_a_jugar % 5 != 0:
                    print('Ingrese un múltiplo de 5.')
                elif monto_a_jugar < 0:
                    print('ingrese un valor valido (>= 0).')
                # Incluimos la opcion de volver al menu
                elif monto_a_jugar == 0:
                    break

            # Si el jugador no desea volver al menu, inicia la mano
            if monto_a_jugar != 0:
                total_apuestas += monto_a_jugar
                mano_jugador = ()
                mano_crupier = ()

                # El jugador recibe dos cartas y se actualiza su puntaje
                for _ in range(2):
                    mano_jugador, puntos_jugador = dar_carta(mano_jugador, VALORES, PALOS, FIGURAS, puntos_jugador)

                # Se define si existió Nlack Jack natural
                if puntos_jugador == 21:
                    bj_natural = True
                    manos_bj_natural += 1

                # Le damos una carta al crupier
                mano_crupier, puntos_crupier = dar_carta(mano_crupier, VALORES, PALOS, FIGURAS, puntos_jugador)

                # Se muestran las manos del jugador y del crupier:
                mostrar_cartas(mano_jugador, 'jugador')
                print(f'Tus puntos son: {puntos_jugador}')
                separador(20, False)
                mostrar_cartas(mano_crupier, 'crupier')

                # El jugador indica si desea recibir otra carta:
                otra_carta = input('Desea recibir otra carta? [s/n]: ')
                separador(20, True)
                while otra_carta == 's' or otra_carta == 'S':
                    mano_jugador, puntos_jugador = dar_carta(mano_jugador, VALORES, PALOS, FIGURAS, puntos_jugador)

                    # Si el jugador se pasa o consigue 21 puntos, no puede pedir mas cartas
                    if puntos_jugador > 21:
                        print('Te has pasado de 21 puntos.')
                        puntos_jugador = 0
                        break
                    elif puntos_jugador == 21:
                        print('Tienes 21 puntos!')
                        break
                    else:
                        mostrar_cartas(mano_jugador, 'jugador')
                        otra_carta = input(f'Tu puntaje actual es de {puntos_jugador} deseas otra carta? [s/n]: ')
                    separador(20, True)

                # El crupier recibe cartas mientras su puntaje sea menor o igual a 16
                while puntos_crupier <= 16:
                    mano_crupier, puntos_crupier = dar_carta(mano_crupier, VALORES, PALOS, FIGURAS,
                                                             puntos_crupier)

                    # En su segunda carta, se verifica si hay Black Jack natural
                    if puntos_jugador == 21 and len(mano_jugador) == 2:
                        bj_natural_crupier = True
                    elif puntos_crupier > 21:
                        puntos_crupier = 0
                        break

                # Se determina el resultado de la mano, teniendo en cuenta los puntajes y BJ naturales
                if puntos_jugador > puntos_crupier or (puntos_jugador == puntos_crupier and bj_natural
                                                       and not bj_natural_crupier):
                    # Se carga el mensaje para mostrar que gano el jugador
                    mensaje_ganador = f'Ha ganado el jugador con {puntos_jugador} puntos contra {puntos_crupier} ' \
                                      f'puntos del crupier.'

                    # Se actualizan las variables del jugador
                    acumulado += monto_a_jugar
                    victorias += 1
                    racha_actual += 1
                    if racha_actual > racha_mas_larga:
                        racha_mas_larga = racha_actual
                elif puntos_jugador == puntos_crupier and puntos_jugador != 0 and bj_natural == bj_natural_crupier:
                    # Cargamos un mensaje para mostrar que hubo empate
                    mensaje_ganador = f'Ha habido un empate! Ambos tienen {puntos_jugador} puntos.'
                else:
                    # Se carga el mensaje para mostrar que gano el crupier (también válido si ambos se pasan)
                    mensaje_ganador = f'Ha ganado el crupier con {puntos_crupier} puntos contra {puntos_jugador} ' \
                                      f'puntos del jugador'

                    # Se actualizan las variables del jugador
                    acumulado -= monto_a_jugar
                    derrotas += 1
                    if racha_actual > racha_mas_larga:
                        racha_mas_larga = racha_actual
                    racha_actual = 0
                    if monto_a_jugar > mayor_perdida:
                        mayor_perdida = monto_a_jugar

                # Se actualiza el monto máximo si corresponde
                if acumulado > monto_max:
                    monto_max = acumulado
                print(f'El jugador inició la mano con un monto acumulado de {monto_inicial}')
                print(f'Realizo una apuesta por {monto_a_jugar}')

                separador(20, False)
                mostrar_cartas(mano_jugador, 'jugador')
                separador(20, False)
                mostrar_cartas(mano_crupier, 'crupier')
                separador(20, False)

                print(mensaje_ganador)
                print(f'El monto acumulado del jugador es de {acumulado}')
                input('\nPresione enter para continuar: ')

        # Aquí se ejecuta la opción 3 del programa, se muestran los resultados y se termina con la ejecución.
        elif opcion == 3:

            # Control de division por cero
            if victorias or derrotas != 0:
                porcentaje_victorias = round(victorias / (victorias + derrotas) * 100, 2)
            else:
                porcentaje_victorias = 0

            # Se calcula el monto promedio de las apuestas
            prom_apuestas = total_apuestas / cant_apuestas

            # Se muestran los datos solicitados
            print(f'El porcentaje de victorias del jugador fué de: {porcentaje_victorias}%')
            print(f'La mayor racha de victorias fue: {racha_mas_larga}')
            print(f'La cantidad de manso con BlackJack natural fue: {manos_bj_natural}')
            print(f'El mayor monto alcanzado por el jugador fue: {monto_max}')
            print(f'El promedio de los montos apostados fue: {prom_apuestas}')
            print(f'La mayor perdida del jugador fue de: {mayor_perdida}')

            # Salida del bucle y fin del juego.
            break

        # Si la opcion fue 1 o 2: el bucle no termina y se vuelve a mostrar el menú y cargar la opcion del usuario.
        separador(30, True)
        opcion = mostrar_opciones()

    print('Hasta pronto!')


def run():
    """Raíz del script para evitar problemas de definición al ejecutar las demás funciones."""
    nombre = input('Ingrese su nombre: ')

    monto = 0
    while monto > 100_000 or monto == 0:
        monto = int(input('Ingrese el monto que desea tener de pozo: '))
        if monto > 100_000 or monto == 0:
            print('El valor ingresado es invalido, por favor ingrese un numero entre [1:100000]')

    separador(20, True)
    # Llamada a la función principal del juego
    menu(nombre, monto)


run()
