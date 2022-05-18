# Datos: nombre, valor hora, horas trabajadas

nombre = input("Ingrese el nombre del empleado: ")
valor_hora = float(input("Ingrese el valor hora: "))
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

sueldo = valor_hora * horas_trabajadas

print(f"El empleado {nombre} debe recibir {sueldo}")
