"""
Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.

Por cada habitante se ingresa: sexo (M/F) y edad. La carga de datos finaliza al ingresar cualquier otro valor para sexo.

El programa debe informar:

a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser igual)

b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)

c) Si hay algún varón que supere los 80 años de edad
"""

sexo = input('Ingrese la sexo del primer ciudadano: ')
edad = int(input('Ingrese la edad del ciudadano: '))

mujeres = hombres = mujeres_escolar = 0
hombre_mayor = False

while sexo == 'F' or sexo == 'M':
    if sexo == 'F':
        mujeres += 1
    else:
        hombres += 1

    if sexo == 'F' and 4 < edad < 18:
        mujeres_escolar += 1

    if sexo == 'M' and edad > 80:
        hombre_mayor = True

    sexo = input('Ingrese la sexo del siguiente ciudadano: ')
    edad = int(input('Ingrese la edad del ciudadano: '))

if mujeres > hombres:
    print('Hay mas mujeres que hombres en la población.')
else:
    print('Hay mas hombres que mujeres en la población.')

print(f'Hay {mujeres_escolar} mujeres en edad escolar.')

if hombre_mayor:
    print('Hay al menos un hombre mayor de 80 años en la población.')
else:
    print('No hay ningún hombre mayor de 80 años en la población.')
