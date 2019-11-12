def retrocontador(e):
	print("{},".format(e), end="")
	if e > 0:
		retrocontador(e-1)

retrocontador(10)

# Sumatorio recursivo

def sumatorio (n):
	if n > 0:
		return n + sumatorio(n-1)
	return 0

print(sumatorio(4))

#Ejercicio factorial

def factorial(x):
	if x > 0:
		return x * factorial(x-1)
	return 1

print(factorial(5))
