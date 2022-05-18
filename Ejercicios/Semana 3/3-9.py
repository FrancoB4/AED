"""Una pequeña empresa de informática tiene que desarrollar un sistema de información y para ello tiene un
presupuesto de x pesos para cubrir los costos de crear el sistema. Sabiendo que tiene pensado ganar al menos 17% por
el proyecto, determine cuál es el valor máximo que pueden alcanzar los costos del proyecto. """

budget = float(input('Ingrese el presupuesto: '))
i = budget * .17

print(f'El costo maxim para un presupuesto de {budget} es de {budget - i}')
