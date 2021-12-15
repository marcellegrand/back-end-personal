capitales = {
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Ecuador": "Quito",
    "Chile": "Santiago"
}

print(capitales)
capital = {"Perú": "Lima"}
capitales.update(capital)
capital = {"Colombia": "Bogotá"}
capitales.update(capital)
print(capitales)
capital = capitales.pop("Bolivia","No existe")
print(capital)
capital = capitales.pop("Chile","No existe")
print(capital)
print(capitales)

print(capitales.keys())
print(capitales.values())

for capital in capitales:
    print(capital,"::",capitales[capital])

for clave in capitales.keys():
    print(clave,"=>",capitales[clave])

for valor in capitales.values():
    print(valor)
    
for clave,valor in capitales.items():
    print(clave,"--",valor)



