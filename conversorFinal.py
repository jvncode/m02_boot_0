class Termometro():

	def __init__(self):
		self.__temperatura = 0
		self.__unidadM = "C"

	def __str__(self):
		return "{}º {}".format(self.__temperatura, self.__unidadM)

	def unidadMedida(self, uniM = None):
		if uniM == None:
			return self.__unidadM
		else:
			if uniM == "F" or uniM == "C" or uniM == "K":
				self.__unidadM = uniM

	def temperatura(self, temperatura=None):
		if temperatura == None:
			return self.__temperatura
		else:
			self.__temperatura = temperatura

	def __conversorCelsiusFahrenheit(self, temperatura, unidad):
		if unidad == "C":
			f = temperatura * (9/5) + 32
			return "La temperatura en grados Fahrenheit es {}".format(round(f,2))
		elif unidad == "F":
			c = (temperatura - 32) * (5/9)
			return "La temperatura en grados Celsius es {}".format(round(c,2))
		

	def __conversorKelvinCelsius(self, temperatura, unidad):
		if unidad == "K":
			c = (self.__temperatura - 273.15)
			return "La temperatura en grados Celsius es {}".format(round(c,2))
		elif unidad == "C":
			k = (self.__temperatura + 273.15)
			return "La temperatura en grados Kelvin es {}".format(round(k,2))
		else:
			return "Unidad incorrecta"
		

	def __conversorFahrenheitKelvin(self, temperatura, unidad):
		if unidad == "F":
			k = (self.__temperatura + 459.67) * (5/9)
			return "La temperatura en grados Kelvin es {}".format(round(k,2))
		elif unidad == "K":
			f = 1.8 * (self.__temperatura - 273.15) + 32
			return "La temperatura en grados Fahrenheit es {}".format(round(f,2))
		else:
			return "Unidad incorrecta"


	def mide(self, uniM=""):
		uniM = uniM.upper()

		if uniM == "" or uniM == self.__unidadM or uniM not in "C, F, K":
			return self.__str__()

		elif uniM == "C":
			if self.__unidadM == "F":
				return self.__conversorCelsiusFahrenheit(self.__temperatura, self.__unidadM)
			else:
				return self.__conversorKelvinCelsius(self.temperatura, self.__unidadM)

		elif uniM == "F":
			if self.__unidadM == "C":
				return self.__conversorCelsiusFahrenheit(self.__temperatura, self.__unidadM)
			else:
				return self.__conversorFahrenheitKelvin(self.__temperatura, self.__unidadM)

		elif uniM == "K":
			if self.__unidadM == "C":
				return self.__conversorKelvinCelsius(self.__temperatura, self.__unidadM)
			else:
				return self.__conversorFahrenheitKelvin(self.__temperatura, self.__unidadM)
		else:
			return self.__str__()
