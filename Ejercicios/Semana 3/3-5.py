"""Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen, para cierto candidato:
apellido, nombre y cantidad de votos. Luego presentar en pantalla un resumen que muestre: iniciales del candidato,
cantidad de votos entre paréntesis, y debajo una línea con tantas "x" como votos obtenidos (por ejemplo,
el candidato obtuvo 4 votos, deberá aparecer una línea como esta: "xxxx" con cuatro letras "x") (Asumimos que en el
centro vecinal no hay demasiados electores, de forma que podamos estar seguros de que no habrá miles o millones de
votos... solo unos pocos para darle sentido al enunciado). """

last_name = input('Apellido del candidato: ')
name = input('Nombre del candidato: ')
votes = int(input('Cantidad de votos del candidato: '))
x = 'x' * votes

print(f'{last_name[0]}{name[0]} ({votes})\n{x}')
