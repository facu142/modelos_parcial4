import os
import pickle

import registro

NOMBRE_ARCHIVO = 'riegos.bin'


def mostrar_menu():
	print('1- Crear vector')
	print('2- Mostrar vector')
	print('3- Buscar riego por ph')
	print('4- Mostrar riegos por ph y conductividad')
	print('5- Generar archivo ')
	print('6- Mostrar contenido del arhivo (solo con ph = 1, 3 o 5)')
	print('7- Generar vector a partir del archivo')
	print('8- Salir ')


def add_in_order_codigo(riegos, nuevo_riego):
	izq = 0
	der = len(riegos) - 1
	pos = len(riegos)

	while izq <= der:
		c = (izq + der) // 2

		if riegos[c].codigo == nuevo_riego.codigo:
			pos = c
			break
		if riegos[c].codigo > nuevo_riego.codigo:
			der = c - 1
		else:
			izq = c + 1

	if izq > der:
		pos = izq

	riegos[pos:pos] = [nuevo_riego]


def generar_riegos(cantidad_riegos):
	riegos = []
	for i in range(cantidad_riegos):
		nuevo_riego = registro.crear_riego_aleatorio()
		add_in_order_codigo(riegos, nuevo_riego)

	return riegos


def mostrar_riegos(riegos):
	print('\n** LISTADO DE RIEGOS **\n')
	for riego in riegos:
		print(riego)


def buscar_riego_por_ph(riegos, ph):
	for riego in riegos:
		if riego.ph == ph:
			return riego

	return -1


def generar_matriz(filas, columnas):
	mat = [[0] * columnas for f in range(filas)]
	return mat


def acumular_volumenes(mat, riegos):
	for riego in riegos:
		mat[riego.ph - 1][riego.conductividad - 1] += riego.volumen


def mostrar_matriz(mat):
	filas = len(mat)
	columnas = len(mat[0])

	for f in range(filas):
		for c in range(columnas):
			if mat[f][c] > 0:
				print(f'PH {f + 1}  CONDUCTIVIDAD {c + 1} => {mat[f][c]}')


def generar_archivo(nombre_archivo, riegos):
	archivo = open(nombre_archivo, 'wb')
	cont = 0
	for riego in riegos:
		cont += 1
		pickle.dump(riego, archivo)

	archivo.close()
	print(f'\nSe ha creado el archivo {nombre_archivo} con {cont}registros\n')


def mostrar_archivo(nombre_archivo):
	if os.path.exists(nombre_archivo):

		archivo = open(nombre_archivo, 'rb')
		tam = os.path.getsize(nombre_archivo)

		while archivo.tell() < tam:
			riego = pickle.load(archivo)
			if riego.ph == 1 or riego.ph == 3 or riego.ph == 5:
				print(riego)

		archivo.close()

	else:
		print(f'No existe el archivo con el nombre {nombre_archivo}')


def generar_vector_del_archivo(nombre_archivo):
	riegos = []

	if os.path.exists(nombre_archivo):
		archivo = open(nombre_archivo, 'rb')
		tam = os.path.getsize(nombre_archivo)

		while archivo.tell() < tam:
			riego = pickle.load(archivo)
			riegos.append(riego)

		archivo.close()

	return riegos


def principal():
	riegos = []
	mostrar_menu()
	opc = int(input('Ingrese una opcion: '))

	while opc != 8:
		if opc == 1:
			n = int(input('Cantidad de riegos a generar: '))
			riegos = generar_riegos(n)
		elif opc == 2:
			if len(riegos) != 0:
				mostrar_riegos(riegos)
			else:
				print('\nDebe cargar el vector primero!\n')
		elif opc == 3:
			if len(riegos) != 0:
				ph = int(input('ph a buscar: '))
				riego_con_x_ph = buscar_riego_por_ph(riegos, ph)
				if riego_con_x_ph != 1:
					print(f'Se ha encontrado un riego con ph {ph}\n')
					print(riego_con_x_ph)
					print()
				else:
					print(f'\nNo se ha encontrado un riego con ph {ph}\n')
			else:
				print('\nDebe cargar el vector primero!\n')
		elif opc == 4:
			mat = generar_matriz(filas=10, columnas=5)
			acumular_volumenes(mat, riegos)
			mostrar_matriz(mat)
		elif opc == 5:
			generar_archivo(NOMBRE_ARCHIVO, riegos)
		elif opc == 6:
			mostrar_archivo(NOMBRE_ARCHIVO)
		elif opc == 7:
			print()
			riegos = generar_vector_del_archivo(NOMBRE_ARCHIVO)
			print(f'Se cargaron {len(riegos)} riegos al vector') if len(riegos) != 0 else print('no se cargaron riegos')
			print()

		mostrar_menu()
		opc = int(input('Ingrese una opcion: '))


if __name__ == '__main__':
	principal()
