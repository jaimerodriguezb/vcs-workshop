

class Command:
	'''
	Clase base para implemantar los commandos que ejecutan
	las operaciones matematicas de la calculadora.
	'''
	def __init__(self,a,b):
	   self.a = a
	   self.b = b

	def execute(self):
	'''
	Por favor sobreescribir este método en cada commando.
	'''
		raise Exception('Overwrite this one pls')

# Implementar comandos

