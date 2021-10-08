import random

letras = 'abcdefghijklmnopqrstuvwxyz'


class Extraccion:
	def __init__(self, codigo, peso, descripcion, volumen):
		self.codigo = codigo
		self.peso = peso
		self.descripcion = descripcion
		self.volumen = volumen

	def __str__(self):
		return f' Codigo:{self.codigo} Peso{self.peso} Desc:{self.descripcion} Volumen:{self.volumen} '


def crear_extraccion_aleatoria():
	codigo = random.randint(100, 999)
	peso = random.randint(1, 10)
	descripcion = random.choice(letras)
	volumen = random.randint(1, 20)

	return Extraccion(codigo, peso, descripcion, volumen)
