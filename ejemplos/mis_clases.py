"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class AutosClasicos:
    nombre = ''
    placa = ''
    color = ''
    motor = 0

    def __init__(self, n, p, c, m):
        self.nombre = n
        self.placa = p
        self.color = c
        self.motor = m

    def __str__(self):
        cadena = "Nombre carro: {}\nPlaca: {}\nColor: {}\nMotor: {}".format(
            self.nombre, self.placa, self.color, self.motor)
        return cadena

# clase 02

class ArrozConPollo:
    tipo = ''
    cantArroz = 0
    extra = ''

    def __init__(self, t, cnt, ex):
        self.tipo = t
        self.cantArroz = cnt
        self.extra = ex

    def __str__(self):
        cadena = "ARROZ CON POLLITO\nTipo de pollo: {}\nCantidad de Arroz: {}\nExtra: {}".format(
            self.tipo, self.cantArroz, self.extra)
        return cadena
