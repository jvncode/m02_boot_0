def maxi(*l):
	if len(l) == 0:
		return 0

	m = l[0]

	for ix in range(1, len(l)):
		if l[ix] > m:
			m = l[ix]

	return m

def mini(*l):
	if len(l) == 0:
		return 0

	m = l[0]

	for ix in range(1, len(l)):
		if l[ix] < m:
			m = l[ix]

	return m


def media(*l):
	if len(l) == 0:
		return 0

	suma = 0
	for valor in l:
		suma += valor

	return suma / len(l)

funciones = {
	"max": maxi,
	"min": mini,
	"med": media
}

def returnF(nombre):
	nombre = nombre.lower()
	if nombre in funciones.keys():
		return funciones[nombre]

	return None

# A continuación la función returnF devolverá el nombre de otra función.
print(returnF("max"))

# Si quiero que la función "max" se ejecute a través de la función "returnF" escribiré lo siguiente:
print(returnF("max")(1, 3, -1, 15, 9))

# Si quiero que la función "min" se ejecute a través de la función "returnF" escribiré lo siguiente:
print(returnF("min")(1, 3, -1, 15, 9))

# Si quiero que la función "med" se ejecute a través de la función "returnF" escribiré lo siguiente:
print(returnF("med")(1, 3, -1, 15, 9))
