"""En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología. El presupuesto anual del
hospital se reparte de la siguiente manera:

    Área:       Presupuesto
* Urgencias:       37%
* Pediatría:       42%
* Traumatología:   21%

Cargar por teclado el monto del presupuesto total del hospital, y calcular y mostrar el monto que recibirá cada área.
"""

total_budget = float(input('Ingrese el presupuesto total: '))

emergencies = total_budget * .37
pediatrics = total_budget * .42
traumatology = total_budget * .21

print(f'Urgencias: {emergencies}\nPediatría: {pediatrics}\nTraumatología: {traumatology}')
