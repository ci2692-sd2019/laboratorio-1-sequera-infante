'''

insertion.py

Descripcion: programa que contiene el algoritmo insertion sort.

Estudiantes: Alexis Infante y Keyber Sequera

Ultima fecha de modificacion: 20/09/2019

'''

# Definimos el algoritmo insertion sort:

def insertionsort(lista,n):

	for i in range(1,n):
		j = lista[i]
		k = i-1
		while k>=0 and j<lista[k]:
			lista[k+1] = lista[k]
			k = k-1
		lista[k+1] = j

	return lista