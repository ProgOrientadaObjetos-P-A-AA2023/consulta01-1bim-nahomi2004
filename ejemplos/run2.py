"""

"""
# Crear dos objetos de la clase 02

from mis_clases import ArrozConPollo

# objeto 01

# crear

pollito1 = ArrozConPollo("Broster",3,"Platanitos fritos")

# Presentar objeto; usar el método __st__

print(str(pollito1))

# objeto 02

print("¿Qué tipo de pollito desea?")
tipo = input()
print("¿Qué cantida de arroz desea? (Cucharones)?")
cant = int(input())
print("Escriba el acompañado:\nPuede ser platanitos, guata, menestra")
extra = input()

# crear ingresando valores por teclado

pollito2 = ArrozConPollo(tipo,cant,extra)

# Presentar objeto; usar el método __st__

print(str(pollito2))


