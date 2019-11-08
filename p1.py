def sumaTodos(limitTo):
	resultado = 0
	for i in range(0, limitTo+1):
		resultado += i

	return resultado

def sumaTodosLosCuadrados(limitTo):
	resultado = 0
	for i in range(limitTo+1):
		resultado += i * i

	return resultado

print(sumaTodos(100))
print(sumaTodosLosCuadrados(3))

#Demo Función de 1ª clase

addAll = sumaTodos
print(addAll(100))

# addAll será una función de 1ª clase
