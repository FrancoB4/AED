pies = float(input("Inserte una medida en pies: "))

yardas = pies / 3
pulgadas = pies * 12
centimetros = pulgadas * 2.54
metros = centimetros / 100

print(f"""
La tabla de conversion para {pies} pies es:
- Yardas: {yardas}
- Pulgadas: {pulgadas}
- Centimetros: {centimetros}
- Metros: {metros}
""")
