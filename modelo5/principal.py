import os
import pickle
import registro

NOMBRE_ARCHIVO = 'medicamentos.bin'


def mostrar_menu():
	print('1- Cargar medicamentos')
	print('2- Mostra vector')
	print('3- Crear archivo')
	print('4- Mostrar archivo')
	print('5- Buscar medicamento por nombre')
	print('6- Mostrar cantidad medicamentos por presentacion')
	print('7- Salir')


def add_in_order_numero(medicamentos, nuevo_medicamento):
	izq = 0
	der = len(medicamentos) - 1
	pos = len(medicamentos)

	while izq <= der:
		c = (izq + der) // 2
		if medicamentos[c].numero == nuevo_medicamento.numero:
			pos = c
			break
		if nuevo_medicamento.numero < medicamentos[c].numero:
			der = c - 1
		else:
			izq = c + 1

	if izq > der:
		pos = izq

	medicamentos[pos:pos] = [nuevo_medicamento]


def cargar_vector(n):
	medicamentos = []
	for i in range(n):
		nuevo_medicamento = registro.crear_registro_aleatorio()
		add_in_order_numero(medicamentos, nuevo_medicamento)

	return medicamentos


def mostrar_vector(medicamentos):
	print('\nListado de medicamentos\n')
	for medicamento in medicamentos:
		print(medicamento)
	print()


def crear_archivo(nombre_archivo, medicamentos):
	importe_max = int(input('Importe maximo a facturar: '))
	archivo = open(nombre_archivo, 'wb')
	cont = 0

	for medicamento in medicamentos:
		if (medicamento.importe == 1 or medicamento.importe == 0) and medicamento.precio < importe_max:
			cont += 1
			pickle.dump(medicamento, archivo)

	print(f'\nSe ha creado el archivo {nombre_archivo} con {cont} registros..\n')
	archivo.close()


def mostrar_archivo(nombre_archivo):
	if os.path.exists(nombre_archivo):
		archivo = open(nombre_archivo, 'rb')
		tam = os.path.getsize(nombre_archivo)

		print('\nLista de medicamentos en el archivo\n')
		while archivo.tell() < tam:
			medicamento = pickle.load(archivo)
			print(medicamento)

		archivo.close()
	else:
		print(f'no existe el archivo con el nombre {nombre_archivo}')


def buscar_medicamento_por_nombre(medicamentos, nombre):
	for medicamento in medicamentos:
		if medicamento.nombre == nombre:
			return medicamento

	return -1


def generar_matriz(filas, columnas):
	return [[0] * columnas for f in range(filas)]


def acumular_med_tipo_y_presentacion(medicamentos, mat):
	for medicamento in medicamentos:
		mat[medicamento.importe][medicamento.presentacion] += 1


def mostrar_mat(mat):
	filas = len(mat)
	columnas = len(mat[0])

	for f in range(filas):
		for c in range(columnas):
			if mat[f][c] != 0:
				print(f'TIPO {f}; PRESENTACION:{c} => {mat[f][c]} ')


def principal():
	medicamentos = []

	mostrar_menu()
	opc = int(input('Ingrese la opcion: '))

	while opc != 7:
		if opc == 1:
			n = int(input('Cantidad de medicamtos a crear: '))
			medicamentos = cargar_vector(n)
		elif opc == 2:
			mostrar_vector(medicamentos)
		elif opc == 3:
			crear_archivo(NOMBRE_ARCHIVO, medicamentos)
		elif opc == 4:
			mostrar_archivo(NOMBRE_ARCHIVO)
		elif opc == 5:
			nombre = input('Ingrese el nombre a buscar: ')

			medicamento_encontrado = buscar_medicamento_por_nombre(medicamentos, nombre)

			if medicamento_encontrado != 1:
				print('\nSe encontro el medicamento\n')
				print(medicamento_encontrado)
				print()
			else:
				print(f'No se encontro el medicamento con nombre {nombre}')
		elif opc == 6:
			mat = generar_matriz(filas=25, columnas=10)
			acumular_med_tipo_y_presentacion(medicamentos, mat)
			mostrar_mat(mat)
		else:
			print('Ingrese una opcion correcta')

		mostrar_menu()
		opc = int(input('Ingrese la opcion: '))


if __name__ == '__main__':
	principal()
