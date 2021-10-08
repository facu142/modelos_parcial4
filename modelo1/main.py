import registro_paquete
import os
import pickle

NOMBRE_ARCHIVO = 'paquetes.bin'


def mostrar_menu():
	print('1- Cargar arreglo ')
	print('2- Mostrar arreglo')
	print('3- Buscar paquete por apellido ')
	print('4- Matriz')
	print('5- Crear archivo a partir de un precio minimo')
	print('6- Mostrar archivo creado')
	print('7- Salir')


def add_in_order_n_id(paquetes, nuevo_paquete):
	n = len(paquetes)
	pos = n
	izq = 0
	der = n - 1

	while izq <= der:
		c = (izq + der) // 2
		if paquetes[c].n_id == nuevo_paquete.n_id:
			pos = c
			break

		if nuevo_paquete.n_id < paquetes[c].n_id:
			der = c - 1
		else:
			izq = c + 1

	if izq > der:
		pos = izq

	paquetes[pos:pos] = [nuevo_paquete]


def cargar_paquetes(paquetes, n):
	for i in range(n):
		nuevo_paquete = registro_paquete.crear_paquete_aleatorio()
		add_in_order_n_id(paquetes, nuevo_paquete)

	return paquetes


def mostrar_paquetes(paquetes):
	for paquete in paquetes:
		print(paquete)


def calcular_importe_origen_destino(paquetes):
	filas = 15  # Origen (ciudad)
	columnas = 20  # Destino (pais)

	mat = [[0] * columnas for f in range(filas)]

	# Acumular

	for paquete in paquetes:
		mat[paquete.origen][paquete.destino] += paquete.precio

	# Mostrar los valores entre el rango a, b
	print('Ingrese el rango:')
	a = int(input('Minimo: '))
	b = int(input('Maximo: '))

	for f in range(len(mat)):
		for c in range(len(mat[0])):
			if mat[f][c] > a and mat[f][c] < b:
				print(f' Origen:{f} Destino:{c} IMPORTE =>  {mat[f][c]}')


def buscar_paquete_por_apellido(paquetes, apellido):
	izq = 0
	der = len(paquetes) - 1

	while izq <= der:
		c = (izq + der) // 2

		if paquetes[c].apellido == apellido:
			return c

		if paquetes[c].apellido < apellido:
			der = c - 1
		else:
			izq = c + 1

	return -1


def crear_archivo(nombre_archivo, vec, precio_minimo):
	archivo = open(nombre_archivo, "wb")
	cont = 0
	for reg in vec:
		if reg.precio > precio_minimo:
			cont += 1
			pickle.dump(reg, archivo)
	archivo.close()
	print(f'Se creo el archivo {nombre_archivo} con {cont} registros\n')


def leer_archivo(nombre_archivo):
	if os.path.exists(nombre_archivo):
		archivo = open(nombre_archivo, 'rb')
		tam = os.path.getsize(nombre_archivo)

		while archivo.tell() < tam:
			paquete = pickle.load(archivo)
			print(paquete)
		archivo.close()
	else:
		print(f'No existe archivo con el nombre {nombre_archivo}')


def principal():
	mostrar_menu()
	opc = int(input('Ingrese una opcion'))
	paquetes = []

	while opc != 7:
		if opc == 1:
			n = int(input('Cantidad paquetes a generar: '))
			paquetes = cargar_paquetes(paquetes, n)
		elif opc == 2:
			if len(paquetes) != 0:
				mostrar_paquetes(paquetes)
			else:
				print('No hay paquetes en el vector')
		elif opc == 3:
			if len(paquetes) != 0:
				apellido = input('Apellido a buscar: ')
				indice = buscar_paquete_por_apellido(paquetes, apellido)
				if indice != -1:
					print('Se ha encontrado un paquete')
					print(paquetes[indice])
					print()
				else:
					print(f'No se ha encontrado un registro con el apellido {apellido} ')
			else:
				print('No hay paquetes en el vector')
		elif opc == 4:
			if len(paquetes) != 0:
				calcular_importe_origen_destino(paquetes)
			else:
				print('No hay paquetes en el vector')
		elif opc == 5:
			p = int(input('precio minimo para guardar en archivo: '))
			crear_archivo(NOMBRE_ARCHIVO, paquetes, p)
		elif opc == 6:
			leer_archivo(NOMBRE_ARCHIVO)
		else:
			print('Ingrese una opcion valida')

		mostrar_menu()
		opc = int(input('Ingrese una opcion'))


if __name__ == '__main__':
	principal()
