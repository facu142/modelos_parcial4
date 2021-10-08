import random

nombres = ['Sertal', 'Bayaspirina', 'Cafiaspirina', 'Novalgina', 'Blokium', 'Amoxidal']


class Medicamento:
	def __init__(self, numero, nombre, precio, tipo, presentacion):
		self.numero = numero
		self.nombre = nombre
		self.precio = precio
		self.tipo = tipo
		self.presentacion = presentacion

	def __str__(self):
		return f'NUMERO:{self.numero} NOMBRE:{self.nombre} PRECIO:{self.precio} TIPO:{self.tipo} PRESENTACION{self.presentacion}'


def crear_registro_aleatorio():
	numero = random.randint(100, 999)
	nombre = random.choice(nombres)
	precio = random.randint(500, 5000)
	tipo = random.randint(0, 24)
	presentacion = random.randint(0, 9)

	return Medicamento(numero, nombre, precio, tipo, presentacion)
