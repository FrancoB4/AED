"""
En la disciplina olímpica una de las pruebas más esperadas en la natación es la posta 4x100. En esta disciplina el
equipo ganador registró los siguientes tiempos en cada estilo:

Espalda: 52 segundos 15 centésimas.
Pecho: 1 minuto 2 segundos 75 centésimas.
Mariposa: 59 segundos 80 centésimas.
Libre: 48 segundos 15 centésimas.
Usted debe averiguar el tiempo total de la carrera del equipo ganador y representarlo en minutos, segundos y centésimas.


Para recordar:

1 minutos son 60 segundos.
1 segundo son 100 centésimas.
"""

espalda = input('Tiempo espalda (mm:ss:cc): ')
pecho = input('Tiempo pecho (mm:ss:cc): ')
mariposa = input('Tiempo mariposa (mm:ss:cc): ')
libre = input('Tiempo libre (mm:ss:cc): ')

m1, m2, m3, m4 = int(espalda[:2]), int(pecho[:2]), int(mariposa[:2]), int(libre[:2])
s1, s2, s3, s4 = int(espalda[3:5]), int(pecho[3:5]), int(mariposa[3:5]), int(libre[3:5])
c1, c2, c3, c4 = int(espalda[6:]), int(pecho[6:]), int(mariposa[6:]), int(libre[6:])

cent_total = (m1 + m2 + m3 + m4)*60*100 + (s1 + s2 + s3 + s4)*100 + c1 + c2 + c3 + c4
minutes = cent_total // 6000
seconds = cent_total % 6000 // 100
hundredths = cent_total % 6000 % 100

print(f'El tiempo total fue de {minutes}:{seconds}:{hundredths}')
