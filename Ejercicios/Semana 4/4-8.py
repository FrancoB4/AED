"""Simular un juego en el que se lanzan dos dados.

 Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina."""
import random

n1 = random.randint(1, 6)
n2 = random.randint(1, 6)

if n1 == n2 or (n1 + n2) % 2 == 0:
    print('Ganó el usuario')
else:
    print('Perdió el usuario')
