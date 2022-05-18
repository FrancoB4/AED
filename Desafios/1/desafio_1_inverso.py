horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))

res = segundos + horas * 3600 + minutos * 60

print(f"{horas}:{minutos}:{segundos} es lo mismo que decir: {res}")
