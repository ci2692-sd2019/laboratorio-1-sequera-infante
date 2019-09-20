'''

test_insertion.py

Descripcion: programa que lee los datos de un documento y reordena los datos de
menor a mayor usando el algoritmo insertion sort.

Estudiantes: Alexis Infante y Keyber Sequera

Ultima fecha de modificacion: 20/09/2019

'''

# Importamos la funcion insertionsort desde insertion

from insertion import insertionsort

print("\nPor favor, al documento que contiene a los numeros que desea ordernar llamelo 'lista', este documento debe estar en el formato txt")

print("\nAdemas asegurese de que en cada linea del documento haya un solo numero, para que el programa pueda funcionar correctamente, de lo contrario el programa mostrara un mensaje de error")

# Abrimos el archivo en modo lectura y escritura

f = open("lista.txt","r+")

lineas = f.readlines()

f.closed

# Calculamos la longitud de la lista obtenida, para usarla como limite superior
# para los futuros ciclos que se ejecutaran.

p = len(lineas)

print("\nLos numeros que contiene el archivo son:\n")

for i in range(0,p):

	print(lineas[i])

# Pasamos los datos de str a int, para poder aplicarles el algoritmo insertion sort

for i in range(0,p):
	lineas[i] = int(lineas[i])

arreglo = insertionsort(lineas,p)

print("\nla lista ordenada es: ", lineas)

# En caso de que se tenga que devolver el resultado en otro documento

print("\nDesea que el arreglo obtenido sea almacenado en un documento? (responda si, en caso de querer hacerlo; o no, en caso de no querer hacerlo)")

R = input(str("\nRespuesta: "))

# Con el fin de crear un nuevo documento con los numeros ordenados, convertiremos
# los elementos del arreglo ordenado de int a str.

if R == "si":

	print("\nPor favor cree el documento 'lista ordenada', en formato txt, y vuelva a ejecutar el programa, en caso de que el documento no haya sido creado")

	for i in range(0,p):

		arreglo[i] = str(arreglo[i])

	m = len(lineas)

	g = open("lista ordenada.txt", "r+")

# Se crea un ciclo que haga que se lea cada elemento del arreglo componente a componente
# y que cada elemento se almacene en una variable llamada "numero", este ciclo al final 
# posicionara en el lugar adecuado cada numero de la lista.

	for i in range(0,m):

		numero = ""

		j = 0

		while j<len(arreglo[i]):

			numero = numero+arreglo[i][j]

			j = j+1

		g.write(numero+"\n")

	g.closed

	g = open("lista ordenada.txt", "r+")

	arreglo = g.readlines()

	print("\nLas lineas del nuevo documento donde los elementos estan ordenados son:\n")

	for i in range(0,len(arreglo)):
	
		print(arreglo[i])



