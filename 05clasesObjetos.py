#clasesObjetos.py

# class ClassName(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, arg):
# 		super(ClassName, self).__init__()
# 		self.arg = arg

		##class tab y sale una estructura automatica de clase

# class MyClase:
# 	pass
# 	##escrito manualmente 

# class MixinData(object):
# 	pass
	##lo que escribas entre el parentesisis es lo que heredara

##instancias

#JAVA, C# Y OTROS
#MixinsData obj = new MixinsData();

#PYTHON o RUBY instanacias de un objeto
# obj=MixinsData()
# print(obj)

#PONER EL CONSTRUCTOR ES OPCIONAL, PERO ES RECOMENDABLE PONERLO, PARA INDICAR LOS PARAMETROS,
#DECLARA EL METODO CONTRUCTOR EN PYTHON SE DEFINEN CON LA PALABRA DEF y el __init__ (dos guiones bajos antes de despues del init) es el contructor oficial de la clase

class MixinsData(object):
	def __init__(
		self,
		user="anonimo",
		password="patito",
		port="1234",
		host="localhost",
		db="sqlite3"):

		self.user = user
		self.password = password
		self.port = port
		self.host = host
		self.db = db

	#dar o enviar parametros
	def get_username(self):
		return self.user

	def get_password(self):
		return self.password

	def get_port(self):
		return self.port

	def get_host(self):
		return self.host

	def get_db(self):
		return self.db

usuario = str(input("Nombre del usuario?: "))
password = str(input("Password?: "))

obj = MixinsData(user=usuario, password=password)

print(obj.user)
print(obj.password)

##invocaremos el parametro username
print (obj.get_username()+"Esta hablando")
print (obj.get_password())
print (obj.get_port())
print (obj.get_host())
print (obj.get_db())