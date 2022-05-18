"""Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa una fecha en
formato 'dd/mm/aaaa', y muestre por separado el día, el mes y el año. Ejemplo: si la cadena ingresada es '16/03/2016'
el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'. """

date = input('Ingrese una fecha (dd/mm/aaaa): ')

day, month, year = date[:2], date[3:5], date[6:]

print(f' Dia: {day}\n Mes: {month}\n Año: {year}')
