class Perro():
# Método Constructor (obligatorio)
	def __init__(self, n, e, p):
		self.nombre = n     # ----> Atributos
		self.edad = e       # ----> Atributos
		self.peso = p       # ----> Atributos
# 1er Método
	def ladrar(self):        #el parámetro ´self´siempre es obligatorio en todos los métodos, después se le pueden agregar otros como una función cualquiera
		if self.peso >= 8:
			print("GUAU GUAU")
		else:
			print("guau guau")

# 2do Método (salida de datos)
	def __str__(self):
		return "Perro: {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)


pitufa = Perro("Pitufa", 4, 10)

print(pitufa.nombre)
pitufa.ladrar()
print(pitufa)

# ------------
# Subclases (Herencias)
class PerroAsistencia(Perro):
	def __init__(self, nombre, edad, peso, amo):
		Perro.__init__(self, nombre, edad, peso)
		self.amo = amo               # ----> Atributos
		self.__trabajando = False      # ----> Atributos

	def __str__(self):   #Este método estaría ´sobreescribiendo´ el metodo ´str´de la clase de la que procede
		return "Perro de asistencia de {}".format(self.amo)

	def pasear(self):
		return "{} ayuda a su amo {} a pasear".format(self.nombre, self.amo)

	def ladrar(self):   #Se sobreescribe la función ´ladrar´de la clase procedente
		if self.__trabajando:
			return "Sssshhhh, no puedo ladrar."
		else:
			Perro.ladrar(self)   #Se llama a la clase procedente para que en este caso entre en funcionamiento

	def trabajando(self, valor=None): #Método-función getter/setter
		if valor == None:
			return self.__trabajando
		else:
			self.__trabajando = valor


ranTanPlan = PerroAsistencia("Ran Tan Plan", 5, 8, "Lucky Luck")

print(ranTanPlan)
print(ranTanPlan.pasear())

print(ranTanPlan.ladrar())
