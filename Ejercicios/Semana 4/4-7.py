"""Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. Permitir que un jugador apueste a cara
o cruz y luego informar si acertó o no con su apuesta. """
import random

choice = random.choice(['cara', 'cruz'])

player_choice = input('¿Cara o cruz? ')

if choice == player_choice:
    print('Acertó')
else:
    print('No acertó')
