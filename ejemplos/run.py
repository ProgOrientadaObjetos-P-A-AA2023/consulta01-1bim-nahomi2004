"""

"""
# Crear dos objetos de la clase 01

from mis_clases import AutosClasicos

# objeto 01

# crear

pichirilo = AutosClasicos('Ferby','LAA-5803','Rojo',1200)

# Presentar objeto; usar el método __st__

print(str(pichirilo))

# objeto 02

# crear ingresando valores por teclado

print("Nombre del carro:")
nombre = input()
print("Placa del carro:")
placa = input()
print("Color del carro:")
color = input()
print("Motor del carro:")
motor = int(input())

camaro = AutosClasicos(nombre,placa,color,motor)

# Presentar objeto; usar el método __st__

print(str(camaro))
