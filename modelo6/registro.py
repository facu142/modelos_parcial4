import random

letras = 'abcdefghijklmnopqrstuvwxyz'


class Pelicula:
	def __init__(self, numero, titulo, importe, tipo, pais):
		self.numero = numero
		self.titulo = titulo
		self.importe = importe
		self.tipo = tipo
		self.pais = pais

	def __str__(self):
		return f'NUMERO:{self.numero} TITULO:{self.titulo} IMPORTE:{self.importe} TIPO:{self.tipo} PAIS:{self.pais} '


def crear_registro_aleatorio():
	numero = random.randint(1, 999)
	titulo = random.choice(letras)
	importe = random.randint(1000, 10000)
	tipo = random.randint(0, 9)
	pais = random.randint(0, 19)

	return Pelicula(numero, titulo, importe, tipo, pais)
