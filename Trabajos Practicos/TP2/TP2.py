import random

VALORES = 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
PALOS = 'Diamante', 'Corazones', 'Pica', 'Trébol'
# Esta tupla nos servirá para luego asignar un nombre a las cartas con valor 10.
FIGURAS = 10, 'J', 'Q', 'K'

texto_figura = ''
texto_resultado = ''
texto_mismo_palo = ''


def separador(n, salto):
    """Una función que se utiliza para separar diferentes segmentos de la interfaz."""
    if salto:
        print('\n')
    print('-' * n)


def dar_carta(mano, valores, palos, figuras, puntos):
    nueva_mano = mano
    es_as = False
    carta = random.choice(valores), random.choice(palos)
    if carta[0] == 10:
        carta = carta[0], carta[1], random.choice(figuras)
    elif carta[0] == 11:
        if puntos + 11 > 21:
            carta = 1, carta[1], 'As'
        else:
            carta = carta[0], carta[1], 'As'
        es_as = True
    else:
        carta = carta[0], carta[1], str(carta[0])

    puntos_actualizados = puntos + carta[0]
    nueva_mano += carta,
    return nueva_mano, puntos_actualizados, es_as


def mostrar_opciones():
    """Esta función muestra el menu de opciones y retorna la opcion escogida por el usuario"""
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
    print(f'Mano del {jugador}:')
    for carta in cartas:
        print(f'{carta[2]} de {carta[1]} con un valor de {carta[0]}')


def menu(nombre_jugador, monto):
    """Definimos una función que representa el cuerpo del programa, aquí se recibe la opcion del usuario y se ejecuta
    la alternativa correspondiente a esa opcion.
    """

    # Esta variable acumulará el monto disponible para jugar
    acumulado = monto
    # Declaramos las variables que vamos a mostrar al salir del juego
    victorias = derrotas = racha_mas_larga = racha_actual = manos_bj_natural = cant_apuestas = total_apuestas = \
        mayor_perdida = 0
    monto_maximo = acumulado
    bj_natural = True

    opcion = mostrar_opciones()

    while True:
        if opcion == 1:
            # Aquí se ejecuta la opción 1 (apuesta) del programa.
            apuesta = 0

            # Controlamos que la apuesta cumpla con la condición requerida (debe ser un número positivo y el acumulado)
            # No debe sobrepasar 100000.
            while apuesta + acumulado > 100_000 or apuesta <= 0:
                apuesta = int(input('Ingrese la nueva apuesta: '))

                if apuesta + acumulado > 100_000:
                    print('La apuesta ingresada no es valida porque al monto acumulado sobrepasa el limite (100000)'
                          f'Por favor ingrese una apuesta menor a {100_000 - acumulado}.')
                elif apuesta <= 0:
                    print('La apuesta ingresada no es valida, por favor ingrese una apuesta mayor que cero.')

            # Actualizamos el acumulado y lo imprimimos en consola.
            acumulado += apuesta
            print(f'Su nuevo monto acumulado es de: {acumulado}')
        elif opcion == 2:
            # Aquí se ejecuta la opción 2 del programa, es el desarrollo del juego en sí.
            cant_apuestas += 1
            # Inicialización de las variables de los puntos de cada jugador.
            puntos_jugador, puntos_crupier, monto_a_jugar = 0, 0, 0
            monto_inicial = acumulado

            # Le pedimos al jugador que realice su apuesta
            while monto_a_jugar <= 0 or monto_a_jugar > acumulado or monto_a_jugar % 5 != 0:
                monto_a_jugar = int(input('Su apuesta esta ronda (0 para salir al menú): '))
                separador(20, False)
                if monto_a_jugar > acumulado:
                    print('No dispone de esa cantidad.')
                elif monto_a_jugar % 5 != 0:
                    print('Ingrese un múltiplo de 5.')
                elif monto_a_jugar < 0:
                    print('ingrese un valor valido (>= 0).')
                elif monto_a_jugar == 0:
                    break

            # En esta condición verificamos que el jugador no haya ingresado la opcion de volver al menú.
            if monto_a_jugar != 0:
                total_apuestas += monto_a_jugar
                mano_jugador = ()
                mano_crupier = ()
                # Le damos dos cartas al jugador y actualizamos su puntaje
                mano_jugador, puntos_jugador, hay_as_jugador = dar_carta(mano_jugador, VALORES, PALOS, FIGURAS, 0)
                mano_jugador, puntos_jugador, hay_as_jugador = dar_carta(mano_jugador, VALORES, PALOS, FIGURAS,
                                                                         puntos_jugador)

                # Le damos una carta al crupier
                mano_crupier, puntos_crupier, hay_as_crupier = dar_carta(mano_crupier, VALORES, PALOS, FIGURAS, 0)

                # Mostramos las cartas que se han repartido:
                mostrar_cartas(mano_jugador, 'jugador')
                print(f'Tus puntos son: {puntos_jugador}')

                separador(20, False)

                mostrar_cartas(mano_crupier, 'crupier')

                otra_carta = input('Desea recibir otra carta? [s/n]: ')
                separador(20, True)
                while otra_carta == 's' or otra_carta == 'S':
                    mano_jugador, puntos_jugador, hay_as_jugador = dar_carta(mano_jugador, VALORES, PALOS, FIGURAS,
                                                                             puntos_jugador)
                    if puntos_jugador > 21:
                        if hay_as_jugador:
                            print('Hay as')
                            break
                        else:
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

                while puntos_crupier <= 16:
                    mano_crupier, puntos_crupier, hay_as_crupier = dar_carta(mano_crupier, VALORES, PALOS, FIGURAS,
                                                                             puntos_crupier)

                    if puntos_crupier > 21:
                        if hay_as_crupier:
                            pass
                        else:
                            puntos_crupier = 0
                            break

                if puntos_jugador > puntos_crupier:
                    # Cargamos un mensaje para mostrar que gano el jugador
                    mensaje_ganador = f'Ha ganado el jugador con {puntos_jugador} puntos contra {puntos_crupier} ' \
                                      f'puntos del crupier.'

                    # Actualizamos las variables del jugador
                    acumulado += monto_a_jugar
                    victorias += 1
                    racha_actual += 1
                    if racha_actual > racha_mas_larga:
                        racha_mas_larga = racha_actual
                elif puntos_jugador == puntos_crupier and puntos_jugador != 0:
                    # Cargamos un mensaje para mostrar que hubo empate
                    mensaje_ganador = f'Ha habido un empate! Ambos tienen {puntos_jugador} puntos.'
                else:
                    # Si el crupier tiene mas puntos que el jugador o ambos se pasan de 21, gana el crupier y se
                    # Crea el mensaje para mostrar
                    mensaje_ganador = f'Ha ganado el crupier con {puntos_crupier} puntos contra {puntos_jugador} ' \
                                      f'puntos del jugador'
                    acumulado -= monto_a_jugar
                    derrotas += 1
                    racha_actual = 0
                    if monto_a_jugar > mayor_perdida:
                        mayor_perdida = monto_a_jugar

                print(f'El jugador inició la mano con un monto acumulado de {monto_inicial}')
                print(f'Realizo una apuesta por {monto_a_jugar}')

                separador(20, False)
                mostrar_cartas(mano_jugador, 'jugador')
                separador(20, False)
                mostrar_cartas(mano_crupier, 'crupier')
                separador(20, False)

                print(mensaje_ganador)
                print(f'El monto acumulado del jugador es de {acumulado}')
                input('\nPresione enter para continuar')
        elif opcion == 3:
            # Aquí se ejecuta la opción 3 del programa, se muestran los resultados y se termina con la ejecución.
            if victorias or derrotas != 0:
                porcentaje_victorias = round(victorias / (victorias + derrotas) * 100, 2)
            else:
                porcentaje_victorias = 0
            prom_apuestas = total_apuestas / cant_apuestas

            print(f'El porcentaje de victorias del jugador fué de: {porcentaje_victorias}%')
            print(f'La mayor racha de victorias fue: {racha_mas_larga}')
            print(f'La cantidad de manso con BlackJack natural fue: {manos_bj_natural}')
            print(f'El promedio de los montos apostados fue: {prom_apuestas}')
            print(f'La mayor perdida del jugador fue de: {mayor_perdida}')

            # Salimos del bucle para terminar con la ejecución del programa.
            break

        # Si la opción ingresada fue 1 o 2, el bucle no termina y se vuelve a mostrar el menú y cargar la opcion del
        # usuario.
        separador(30, True)
        opcion = mostrar_opciones()

    print('Hasta pronto!')


def run():
    """Creamos una function que contenga la raíz del script para evitar problemas de definición al ejecutar las
    demás funciones
    """
    nombre = input('Ingrese su nombre: ')

    monto = 0
    while monto > 100_000 or monto == 0:
        monto = int(input('Ingrese el monto que desea tener de pozo: '))
        if monto > 100_000 or monto == 0:
            print('El valor ingresado es invalido, por favor ingrese un numero entre [1:100000]')

    separador(20, True)
    menu(nombre, monto)


run()
