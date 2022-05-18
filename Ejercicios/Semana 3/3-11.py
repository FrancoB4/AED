"""Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva enmascarada, mostrando la
primer letra y la última, pero reemplazando los caracteres intermedios por asteriscos.

Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.
"""

word = input('Ingrese una palabra: ')
length = len(word) - 2

print(word[0] + '*'*length + word[-1])
