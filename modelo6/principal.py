import os
import pickle
import registro

NOMBRE_ARCHIVO = 'peliculas.bin'


def mostrar_menu():
	print('1- Cargar peliculas')
	print('2- Mostrar peliculas')
	print('3- Crear archivo')
	print('4- Mostrar archivo')
	print('5- Buscar pelicula por numero')
	print('6- Cantidad de peliculas por pais')
	print('7- Salir')


def add_in_order_nombre(peliculas, nueva_pelicula):
	izq = 0
	der = len(peliculas) - 1
	pos = len(peliculas)

	while izq <= der:
		c = (izq + der) // 2

		if peliculas[c].titulo == nueva_pelicula.titulo:
			pos = c
			break
		if peliculas[c].titulo < nueva_pelicula.titulo:
			izq = c + 1
		else:
			der = c - 1

		if izq > der:
			pos = izq

	peliculas[pos:pos] = [nueva_pelicula]


def crear_vector(n):
	peliculas = []

	for i in range(n):
		nueva_pelicula = registro.crear_registro_aleatorio()
		add_in_order_nombre(peliculas, nueva_pelicula)

	return peliculas


def mostrar_peliculas(peliculas):
	print('\nListado de peliculas\n')
	for pelicula in peliculas:
		print(pelicula)


def crear_archivo(nombre_archivo, peliculas):
	importe_maximo = int(input('\nImporte maximo: '))
	cont = 0
	archivo = open(nombre_archivo, 'wb')

	for pelicula in peliculas:
		if pelicula.pais != 10 and pelicula.importe < importe_maximo:
			cont += 1
			pickle.dump(pelicula, archivo)

	print(f'Se creo el archivo {nombre_archivo} con {cont} registos')
	archivo.close()


def mostrar_archivo(nombre_archivo):
	if os.path.exists(nombre_archivo):
		archivo = open(nombre_archivo, 'rb')
		tam = os.path.getsize(nombre_archivo)
		print('\nDatos en el archivo:\n')

		while archivo.tell() < tam:
			reg = pickle.load(archivo)
			print(reg)
		archivo.close()


def buscar_pelicula_por_nombre(peliculas, nombre):
	for pelicula in peliculas:
		if pelicula.titulo == nombre:
			return pelicula
	return -1


def crear_matriz(filas, columnas):
	return [[0] * columnas for f in range(filas)]


def contar_tipo_y_pais(mat, peliculas):
	for pelicula in peliculas:
		mat[pelicula.tipo][pelicula.pais] += 1


def mostrar_tipo_y_pais(mat):
	filas = len(mat)
	columnas = len(mat[0])

	for f in range(filas):
		for c in range(columnas):
			if mat[f][c] != 0:
				print(f'TIPO:{f} PAIS{c} => {mat[f][c]} ')


def principal():
	peliculas = []

	mostrar_menu()
	opc = int(input('Ingrese la opcion: '))

	while opc != 7:
		if opc == 1:
			n = int(input('Ingrese la cantidad de peliculas a generar: '))
			peliculas = crear_vector(n)
		elif opc == 2:
			mostrar_peliculas(peliculas)
		elif opc == 3:
			crear_archivo(NOMBRE_ARCHIVO, peliculas)
		elif opc == 4:
			mostrar_archivo(NOMBRE_ARCHIVO)
		elif opc == 5:
			nombre = int(input('Nombre a buscar: '))
			pelicula_encontrada = buscar_pelicula_por_nombre(peliculas, nombre)

			if pelicula_encontrada != 1:
				print(f'Se encontro la pelicula con titulo {nombre}')
				print(pelicula_encontrada)
				print()
			else:
				print(f'No se encontro la pelicula con titulo {nombre}')
		elif opc == 6:
			mat = crear_matriz(filas=10, columnas=20)
			contar_tipo_y_pais(mat, peliculas)
			mostrar_tipo_y_pais(mat)

		else:
			print('Ingrese una opcion correcta')

		mostrar_menu()
		opc = int(input('Ingrese la opcion: '))


if __name__ == '__main__':
	principal()
