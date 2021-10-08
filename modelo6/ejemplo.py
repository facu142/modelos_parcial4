import os
import pickle
import registro


def mostrar_menu():
	print('1- ')
	print('2- ')
	print('3- ')
	print('4- ')
	print('5- ')
	print('6- ')
	print('7- Salir')


def principal():

	peliculas = []

	mostrar_menu()
	opc = int(input('Ingrese la opcion: '))

	while opc != 7:
		if opc == 1:
			n = int(input('n: '))
			crear_vector(n)

		elif opc == 2:
			pass
		elif opc == 3:
			pass
		elif opc == 4:
			pass
		elif opc == 5:
			pass
		elif opc == 6:
			pass
		else:
			print('Ingrese una opcion correcta')

		mostrar_menu()
		opc = int(input('Ingrese la opcion: '))


if __name__ == '__main__':
	principal()
