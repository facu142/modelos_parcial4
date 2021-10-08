import os
import pickle

import registro_extraccion

NOMBRE_ARCHIVO = 'extracciones.bin'


def mostrar_menu():
	print('1- Cargar arreglo ')
	print('2- Mostrar arreglo')
	print('3- Mostrar datos de los registros en un rango de peso')
	print('4- Mostrar datos extracciones peso y volumen')
	print('5- Generar archivo con extracciones (volumen > 0)')
	print('6- Mostrar contenido del archivo')
	print('7- Salir')


def add_in_order_descripcion(extracciones, nueva_extraccion):
	n = len(extracciones)
	izq = 0
	der = len(extracciones) - 1
	pos = n

	while izq <= der:
		c = (izq + der) // 2

		if extracciones[c].descripcion == nueva_extraccion.descripcion:
			pos = c
			break
		if nueva_extraccion.descripcion < extracciones[c].descripcion:
			der = c - 1
		else:
			izq = c + 1

	if izq > der:
		pos = izq

	extracciones[pos:pos] = [nueva_extraccion]


def crear_vector_extracciones(n):
	extracciones = []

	for i in range(n):
		nueva_extraccion = registro_extraccion.crear_extraccion_aleatoria()
		add_in_order_descripcion(extracciones, nueva_extraccion)

	return extracciones


def mostrar_extracciones(extracciones):
	print('\n************ LISTADO DE EXTRACCIONES ************\n')
	for extraccion in extracciones:
		print(extraccion)
	print()


def mostrar_extracciones_rango_peso(extracciones, limite_inf, limite_sup):
	print(f'\n************ LISTADO DE EXTRACCIONES Peso:{limite_inf}-{limite_sup}************\n')
	for extraccion in extracciones:
		if extraccion.peso > limite_inf and extraccion.peso < limite_sup:
			print(extraccion)


def generar_matriz(filas, columnas):
	mat = [[0] * columnas for f in range(filas)]
	return mat


def contar_en_mat(extracciones, mat):
	for extraccion in extracciones:
		mat[extraccion.peso - 1][extraccion.volumen - 1] += 1


def mostrar_mat(mat):
	filas = len(mat)
	columnas = len(mat[0])

	for f in range(filas):
		for c in range(columnas):
			if mat[f][c] != 0:
				print(f'PESO {f + 1} Volumen {c + 1} => {mat[f][c]}')


def generar_archivo(nombre_archivo, extracciones, volumen_minimo):
	archivo = open(nombre_archivo, 'wb')
	cont = 0
	for extraccion in extracciones:
		if extraccion.volumen > volumen_minimo:
			cont += 1
			pickle.dump(extraccion, archivo)

	print(f'Se ha creado el archivo {nombre_archivo} con {cont} registros')
	archivo.close()


def mostrar_archivo(nombre_archivo):
	if os.path.exists(nombre_archivo):
		archivo = open(nombre_archivo, 'rb')
		tam = os.path.getsize(nombre_archivo)

		print('\nLISTA EXTRACCION EN ARCHIVO\n')

		while archivo.tell() < tam:
			extraccion = pickle.load(archivo)
			print(extraccion)
		print('\n\n')
		archivo.close()
	else:
		print(f'no existe el archivo {nombre_archivo}')


def principal():
	extracciones = []

	mostrar_menu()
	opc = int(input('Ingrese la opcion: '))

	while opc != 7:
		if opc == 1:
			n = int(input('Cantidad de extracciones a generar: '))
			extracciones = crear_vector_extracciones(n)
		elif opc == 2:
			if len(extracciones) != 0:
				mostrar_extracciones(extracciones)
			else:
				print('No se cargo el vector\n')
		elif opc == 3:
			if len(extracciones) != 0:
				a = int(input('minimo: '))
				b = int(input('maximo: '))
				mostrar_extracciones_rango_peso(extracciones, limite_inf=a, limite_sup=b)
			else:
				print('No se cargo el vector\n')
		elif opc == 4:
			mat = generar_matriz(filas=10, columnas=20)
			contar_en_mat(extracciones, mat)
			mostrar_mat(mat)
		elif opc == 5:
			volumen_minimo = int(input('Volumen minimo: '))
			generar_archivo(NOMBRE_ARCHIVO, extracciones, volumen_minimo)
		elif opc == 6:
			mostrar_archivo(NOMBRE_ARCHIVO)

		mostrar_menu()
		opc = int(input('Ingrese la opcion: '))


if __name__ == '__main__':
	principal()
