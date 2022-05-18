"""Se conoce el monto del salario actual de un empleado, el nombre del empleado y el área funcional al cual
pertenece. Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento del 8% sobre su salario
actual y un descuento de 2.5% por servicios, informando los resultados con el formato que se especifica a continuación:

       Nombre Empleado: xxxxxxxxx            Nuevo Salario: $ xxx

       Área Funcional: xxxxxxxxxxxx

       Salario Actual: $ xxxx
"""

name = input('Ingrese el nombre del empleado: ')
salary = float(input(f'Ingrese el salario de {name}: '))
functional_area = input(f'Ingrese el area funcional de {name}: ')

new_salary = salary * 1.08

print(f'\nNombre Empleado: {name}           Nuevo Salario: {new_salary}\n\nArea Funcional: {functional_area}\n'
      f'\nSalario Actual: {salary}')
