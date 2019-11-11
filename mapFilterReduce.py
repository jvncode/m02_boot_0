lista = [1, 3, -1, 15, 9]

def doble (x):
	return x + x

# Map
listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista) #Esta opción sería la misma que la anterior pero usando el map con una función ya creada anteriormente

# -------------

#Filter
def esPar(x):
	return x % 2 == 0

listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares1 = filter(esPar, lista) #Esta opción sería la misma que la anterior pero usando filter con una función ya creada anteriormente 

#--------------

#Reduce
#Para usar esta función hay que importarla
from functools import reduce

sumatorio = reduce(lambda x,y: x + y, lista) #El resultado es 27
sumatorioDoble= reduce(lambda x,y: x + y*2, lista) #El resutado es 53 (tener en cuenta que la x toma el primer valor de la lista sin realizaar la operación desiganada en la lambda)

suma100 = reduce(lambda x,y: x + y, range(101)) #Resultado 5050

print(listaPares)

print(listaDobles)

print(sumatorio)
print(sumatorioDoble)
print(suma100)