"""Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
cadena de caracteres. El texto finaliza con '.' y se supone que el usuario cargará el punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir
al menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter (a
razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

1 - Determinar la cantidad de palabras que contienen la lera "m" o la letra "o" (minúscula o mayúscula) a partir de
la segunda letra (inclusive) de la palabra. Por ejemplo, en el texto “El Villareal de España juega en un estadio
llamado el Madrigal.” hay 2 palabras cumplen con la condición (“llamado”, “estadio”)

2- Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que contienen al menos 2
digitos. Por ejemplo, en el texto "Los cursos 1K14 y 1K15 rinden en turnos separados." hay 9 palabras y 2 de ellas
cumplen el criterio ("1K14" y "1K15"), por lo tanto el porcentaje es 22.22%

3- Determinar la cantidad de palabras que contienen una vocal (minúscula o mayúscula) en todas las posiciones impares
de dicha palabra. Por ejemplo, en el texto "La imagen incluye una claridad de luces." hay 2 palabras cumplen el
criterio ("imagen" y "una").

4 - Determinar la cantidad de palabras que la expresión "pr" (con cualquiera de sus letras en minúscula o en
mayúscula) pero de forma tal que la secuencia esté presente a partir del tercer caracter (incluido) de la palabra.
Por ejemplo, en el texto "La impronta del problema comprueba su dificultad." hay 2 palabras que cumplen el criterio (
"impronta" y "comprueba"). """


def es_caracter(car):
    return car != ' ' and car != '.'


def es_numero(car):
    return car in '1234567890'


def es_vocal(car):
    return car in 'aeiou'


def porcentaje(parcial, total):
    if total != 0:
        return round(parcial * 100 / total, 2)
    return 0


def main():
    texto = input('Ingrese un texto: ').lower()

    palabras_m_o = total_palabras = dos_digitos = palabras_pr = palabras_vocal_impar = 0
    orden = numeros = 0
    es_p = tiene_om = tiene_pr = False
    vocal_impar = True

    for car in texto:
        if es_caracter(car):
            orden += 1

            if orden >= 2 and car in 'om':
                tiene_om = True

            if es_numero(car):
                numeros += 1

            if orden % 2 != 0 and not es_vocal(car):
                vocal_impar = False

            if car == 'p' and orden >= 3:
                es_p = True
            elif es_p and car == 'r':
                tiene_pr = True
                es_p = False
            else:
                es_p = False
        else:
            total_palabras += 1

            if tiene_om:
                palabras_m_o += 1

            if numeros >= 2:
                dos_digitos += 1

            if vocal_impar:
                palabras_vocal_impar += 1

            if tiene_pr:
                palabras_pr += 1

            orden = numeros = 0
            es_p = tiene_om = tiene_pr = False
            vocal_impar = True

    porcentaje_dos_digitos = porcentaje(dos_digitos, total_palabras)

    print(f' * Palabras que contienen "m" u "o":            | {palabras_m_o}')
    print(f' * Porcentaje palabras con mas de dos dígitos:  | {porcentaje_dos_digitos}%')
    print(f' * Con vocales en todas las pos impares:        | {palabras_vocal_impar}')
    print(f' * Contienen "pr" después de la 3 pos:          | {palabras_pr}')


if __name__ == '__main__':
    main()
