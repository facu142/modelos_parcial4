import random

apellidos = 'abcdefghijklmnopqrstuvwxyz'


class Paquete:
	def __init__(self, n_id, apellido, precio, ortigen, destino):
		self.n_id = n_id
		self.apellido = apellido
		self.precio = precio
		self.origen = ortigen
		self.destino = destino

	def __str__(self):
		return f'id:{self.n_id}, apellido:{self.apellido}, precio:{self.precio}, origen:{self.origen}, destino:{self.destino}'


def crear_paquete_aleatorio():
	n_id = random.randint(1, 100)
	apellido = random.choice(apellidos)
	precio = random.randint(5000, 50000)
	origen = random.randint(0, 14)
	destino = random.randint(0, 19)

	return Paquete(n_id, apellido, precio, origen, destino)
