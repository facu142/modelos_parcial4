import random

letras = 'abcdefghijklmnopqrstuvwxyz'


class Profesional:
	def __init__(self, dni, nombre, importe, tipo_afiliacion, tipo_trabajo):
		self.dni = dni
		self.nombre = nombre
		self.importe = importe
		self.tipo_afiliacion = tipo_afiliacion
		self.tipo_trabajo = tipo_trabajo

	def __str__(self):
		return f' DNI:{self.dni} NOMBRE:{self.nombre} IMPORTE:{self.importe} TIPO_AFILIACION:{self.tipo_afiliacion} ' \
			   f'TIPO_TRABAJO: {self.tipo_trabajo}'

def crear_registro_aleatorio():
	dni = random.randint(10000000, 40000000)
	nombre = random.choice(letras)
	importe = random.randint(1000, 10000)
	tipo_afiliacion = random.randint(0, 4)
	tipo_trabajo = random.randint(0, 14)
	return Profesional(dni, nombre, importe, tipo_afiliacion, tipo_trabajo)
