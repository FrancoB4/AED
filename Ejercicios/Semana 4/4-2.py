"""Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10
dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo. """

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

res = n1 + n2 + n3

if res > 10:
    print(int(res / 2))
else:
    print(res ** 3)
