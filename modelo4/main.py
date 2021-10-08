import os
import pickle
import registro

NOMBRE_ARCHIVO = 'profesionales.bin'


def mostrar_menu():
	print('\n****** Menu de opciones *******')
	print('1- Generar profesionales')
	print('2- Mostrar arreglo profesionales')
	print('3- Buscar profesional por nombre')
	print('4- matriz')
	print('5- Crear archivo')
	print('6- Leer archivo')
	print('7- Salir\n')


def add_in_order_dni(profesionales, nuevo_profesional):
	izq = 0
	der = len(profesionales) - 1
	pos = len(profesionales)

	while izq <= der:
		c = (izq + der) // 2
		if profesionales[c].dni == nuevo_profesional.dni:
			pos = c
			break
		if nuevo_profesional.dni < profesionales[c].dni:
			der = c - 1
		else:
			izq = c + 1

	if izq < der:
		pos = izq

	profesionales[pos:pos] = [nuevo_profesional]


def crear_vector_profesionales(n):
	profesionales = []

	for i in range(n):
		nuevo_profesional = registro.crear_registro_aleatorio()
		add_in_order_dni(profesionales, nuevo_profesional)

	return profesionales


def mostrar_vector(profesionales):
	print('\nLista de profesionales\n')
	for profesional in profesionales:
		print(profesional)
	print()


def buscar_profesional_por_nombre(profesionales, nombre):
	for profesional in profesionales:
		if profesional.nombre == nombre:
			return profesional
	return -1


def crear_matriz(filas, columnas):
	mat = [[0] * columnas for f in range(filas)]

	return mat


def contar_tipo_afil_tipo_trabajo(profesionales, mat):
	for profesional in profesionales:
		mat[profesional.tipo_afiliacion][profesional.tipo_trabajo] += 1


def mostrar_mat(mat):
	filas = len(mat)
	columnas = len(mat[0])

	for f in range(filas):
		for c in range(columnas):
			if mat[f][c] > 0:
				print(f'Alifiacion: {f} - Trabajo: {c} => {mat[f][c]}')


def crear_archivo(nombre_archivo, profesionales):
	archivo = open(nombre_archivo, 'wb')
	cont = 0
	for profesional in profesionales:
		if profesional.tipo_trabajo == 3 or profesional.tipo_trabajo == 4 or profesional.tipo_trabajo == 5:
			cont += 1
			pickle.dump(profesional, archivo)

	archivo.close()

	print(f'Se creo el archivo {nombre_archivo} con {cont} registros')


def mostrar_archivo(nombre_archivo):
	if os.path.exists(nombre_archivo):
		archivo = open(nombre_archivo, 'rb')
		tam = os.path.getsize(nombre_archivo)

		while archivo.tell() < tam:
			reg = pickle.load(archivo)
			print(reg)

		archivo.close()

	else:
		print(f'No existe el archivo con el nombre {nombre_archivo}')


def principal():
	profesionales = []

	mostrar_menu()
	opc = int(input('Ingrese la opcion: '))

	while opc != 7:
		if opc == 1:
			n = int(input('Cantidad de profesionales a generar: '))
			profesionales = crear_vector_profesionales(n)
		elif opc == 2:
			mostrar_vector(profesionales)
		elif opc == 3:
			nombre = input('\nNombre a buscar: ')
			profesional_encontrado = buscar_profesional_por_nombre(profesionales, nombre)
			if profesional_encontrado != -1:
				print(f'Se encontro al profesional con nombre {nombre}')
				print()
		elif opc == 4:
			mat = crear_matriz(filas=5, columnas=15)
			contar_tipo_afil_tipo_trabajo(profesionales, mat)
			mostrar_mat(mat)
		elif opc == 5:
			crear_archivo(NOMBRE_ARCHIVO, profesionales)
		elif opc == 6:
			mostrar_archivo(NOMBRE_ARCHIVO)
		else:
			print('Ingrese una opcion correcta')

		print()
		mostrar_menu()
		opc = int(input('Ingrese la opcion: '))


if __name__ == '__main__':
	principal()
