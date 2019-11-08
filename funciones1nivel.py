def normal(i):
	return i

def cuadrado(x):
	return x * x

# Función de 1er Nivel. El parámetro "f" será una función que complementa a "limitTo".

def sumaTodos(limitTo, f):
	resultado = 0
	for i in range(limitTo+1):
		resultado += f(i)

	return resultado

print(sumaTodos(3, cuadrado))
