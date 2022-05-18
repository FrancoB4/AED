"""Una persona cautivada por los paisajes argentinos se le ocurrió la loca idea de unir los puntos más extremos
(Ushuahia y La Quiaca) en bicicleta, es decir se propuso hacer 3641.3 Km en bicicleta.

Nuestro aventurero efectivamente inició la travesía, pero se accidentó y solo recorrió x metros según su GPS.

Usted debe solicitar ese valor x e informar cuántos kilómetros y metros recorrió nuestro aventurero y qué porcentaje
represento lo recorrido del total de kms a recorrer de Ushuahia a La Quiaca (para el porcentaje usted deberá realizar
los calculos en metros). """

TOTAL_RECORRIDO = 3641.3

metros = int(input('Ingrese la cantidad de metros recorridos: '))

km = metros / 1000
porcentaje = round(km / TOTAL_RECORRIDO * 100, 2)

print(f'Recorrió {km}km, lo que representa un {porcentaje}% del recorrido.')
