"""Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo por un cliente de un
banco y calcular el saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que el interés pactado era de 2.3%
y que el banco cobra una tasa fija de gastos por servicios financieros igual $20 por cuenta """

amount = float(input("Ingrese la cantidad de dinero: "))

i = amount / 100 * 2.3

print(f"La cantidad de dinero al finalizar el plazo sera: {amount + i - 20}")
