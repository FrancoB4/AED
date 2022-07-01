def average(count, division):
    if division != 0:
        return round(count / division, 2)
    return 0


def percentage(parcial, total):
    if total != 0:
        return round(parcial * 100 / total, 2)
    return 0


def is_char(char):
    return char != ' ' and char != '.'


def is_num(char):
    return char in '1234567890'


def is_alphabetical(char):
    return 'a' <= char <= 'z' or char == 'ñ'


def is_vocal(char):
    return char in 'aeiou'


def is_consonant(char):
    return char in 'qwrtypsdfghjklñzxcvbnm'
