"""
La Dirección de Tránsito de Córdoba necesita un programa que permita validar las patentes que se ingresan al sistema.

El programa debe solicitar el ingreso de una patente (sin espacios intermedios) y luego:

Informar si se trata de una patentes en formato antiguo (XXX999) o nuevo (XX999YY)
Verificar que contenga letras y números de acuerdo a lo esperado
"""
patente = input('Patente: ')
pos = 0
ok = True

for char in patente:
    num = (char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7'
           or char == '8' or char == '9' or char == '0')

    if len(patente) == 6 and ((num and pos < 3) or (not num and pos >= 3)):
        ok = False
    elif len(patente) == 7 and ((num and (pos <= 1 or pos >= 5)) or (not num and (2 <= pos < 5))):
        ok = False

    pos += 1

if ok:
    if len(patente) == 6:
        print('Se ha ingresado una patente vieja valida')
    else:
        print('Se ha ingresado una patente nueva valida')
else:
    print('Se ha ingresado una patente invalida')
