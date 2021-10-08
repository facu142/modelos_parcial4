import random


class Riego:
	def __init__(self, volumen, ph, conductividad, codigo_solucion):
		self.volumen = volumen
		self.ph = ph
		self.conductividad = conductividad
		self.codigo = codigo_solucion

	def __str__(self):
		return f'VOL:{self.volumen}; PH:{self.ph}; CONDUCTIVIDAD:{self.conductividad}; CODIGO SOLUCION:{self.codigo}'


def crear_riego_aleatorio():
	volumen = round(random.uniform(1, 10), 2)
	ph = random.randint(1, 10)
	conductividad = random.randint(1, 5)
	codigo = random.randint(100, 999)
	return Riego(volumen, ph, conductividad, codigo)
