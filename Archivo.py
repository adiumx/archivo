import os
import shutil
class Archivo(object):
	"""docstring for Archivo"""
	def __init__(self, nombre, contenido):
		try:
			self.f = open(nombre, 'w')
			self.nombre = nombre
			self.f.write(contenido)
			self.f.close
		except Exception as e:
			#print("No se puede abrir el Archivo", nombre)
			print(e)
	def copiar(self):
		pass
		fuente = input("Archivo fuente: ")
		destino = input("Archivo destino: ")
		shutil.copyfile(fuente, destino)
	def muestra(self):
		self.f = open(self.nombre, 'r')
		for linea in self.f:
			print("{:3}".format(linea))
		self.f.seek(0)
		self.f.close
	def cuentaVocales(self):
		pass
		self.f = open(self.nombre, 'r')
		def vocales(s):
			contador = 0
			for i in range(len(s)):
				pass
				if s[i] in set("aeiouáéíóú"):
					contador += 1
			return contador
		contador = 0
		for linea in self.f:
			pass
			contador += vocales(linea)
		self.f.seek(0)
		self.f.close
		return contador
	def cuentaConsonantes(self):
		self.f = open(self.nombre, 'r')
		def consonantes(s):
			contador = 0
			for i in range(len(s)):
				if s[i].lower() in set("bcdfghjklmnpqrstvwxyz"):
					contador += 1
			return contador
		contador = 0
		for linea in self.f:
			pass
			contador += consonantes(linea)
		self.f.seek(0)
		self.f.close
		return contador
	def cuentaMayus(self):
		self.f = open(self.nombre, 'r')
		def mayus(s):
			contador = 0
			for i in range(len(s)):
				if s[i] in set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
					contador += 1
			return contador
		contador = 0
		for linea in self.f:
			pass
			contador += mayus(linea)
		self.f.seek(0)
		self.f.close
		return contador
	def cuentaMinus(self):
		self.f = open(self.nombre, 'r')
		def minus(s):
			contador = 0
			for i in range(len(s)):
				if s[i] in set("abcdefghijklmnopqrstvwxyz"):
					contador += 1
			return contador
		contador = 0
		for linea in self.f:
			pass
			contador += minus(linea)
		self.f.seek(0)
		self.f.close
		return contador
	def cuentaLineas(self):
		self.f = open(self.nombre, 'r')
		self.f.seek(0)
		print (len(self.f.readlines()))
	def aMin(self):
		pass
		self.f = open(self.nombre, 'r+')
		mensaje = self.f.read()
		mensaje=mensaje.lower()
		print(mensaje)
		self.f.close
		self.f = open(self.nombre, 'w')
		self.f.write(mensaje)
		self.f.seek(0)
		self.f.close
	def aMay(self):
		pass
		self.f = open(self.nombre, 'r+')
		mensaje = self.f.read()
		mensaje=mensaje.upper()
		print(mensaje)
		self.f.close
		self.f = open(self.nombre, 'w')
		self.f.write(mensaje)
		self.f.seek(0)
		self.f.close
	def cuentaPalabras(self):
		pass
		self.f = open(self.nombre, 'r+')
		mensaje = self.f.read()
		a=len(mensaje.split(" "))
		self.f.close
		return a
	def hexadecimal(self):
		pass
		self.f = open(self.nombre, 'r')
		mensaje = self.f.read()
		a=hex(ord(mensaje))
		self.f.close
		return a
	def cuentaSignos(self):
		self.f = open(self.nombre, 'r')
		def signos(s):
			contador = 0
			for i in range(len(s)):
				if s[i] in set("\,\;\:\¿\?\!\¡\(\)\[\]\-\_\*\."):
					contador += 1
					print(s[i])
			return contador
		contador = 0
		for linea in self.f:
			pass
			contador += signos(linea)
		self.f.seek(0)
		self.f.close
		return contador
#main
def switch_demo(argument):
    switcher = {
        1: "1 Crear archivo",
        2: "2 Copiar archivo",
        3: "3 Mostrar",
        4: "4 Cuenta vocales",
        5: "5 Cuenta consonantes",
        6: "6 Cuenta signos de puntuacion",
        7: "7 Cuenta espacios",
        8: "8 Cuenta palabras",
        9: "9 Cuenta lineas",
        10: "10 Cuenta mayusculas",
        11: "11 Cuenta minusculas",
        12: "12 Muestra en hexadecimal",
        13: "13 Convertir a mayusculas",
        14: "14 Convertir a minusculas"
    }
    print (switcher.get(argument, "Invalido"))
n=0
nombre=list()
while n!=15:
	pass
	for x in range(1,15):
		pass
		switch_demo(x)
	n = int(input("Introduce un numero: "))

	if n ==1:
		pass
		nombre = input("Nombre del archivo: ")
		contenido=input("Escribe lo que quieras poner en el archivo: \n")
		archivo = Archivo(nombre, contenido)
	elif n==2:
		pass
		if(len(nombre)!=0):
			archivo.copiar()
		else:
			print("El archivo no existe")
	elif n==3:
		if(len(nombre)!=0):
			archivo.muestra()
		else:
			print("El archivo aun no existe")
	elif n==4:
		if(len(nombre)!=0):
			a=archivo.cuentaVocales()
			print(a)
		else:
			print("El archivo no existe")
	elif n==5:
		if(len(nombre)!=0):
			a=archivo.cuentaConsonantes()
			print(a)
		else:
			print("El archivo no existe")
	elif n==6:
		if(len(nombre)!=0):
			a=archivo.cuentaSignos()
			print(a)
		else:
			print("El archivo no existe")
	elif n==7:
		if(len(nombre)!=0):
			a=archivo.cuentaPalabras()
			print(a-1)
		else:
			print("El archivo no existe")
	elif n==8:
		if(len(nombre)!=0):
			a=archivo.cuentaPalabras()
			print(a)
		else:
			print("El archivo no existe")
	elif n == 9:
		if(len(nombre)!=0):
			a=archivo.cuentaLineas()
			print(a)
		else:
			print("El archivo no existe")
	elif n ==10:
		if(len(nombre)!=0):
			a=archivo.cuentaMayus()
			print(a)
		else:
			print("El archivo no existe")
	elif n ==11:
		if(len(nombre)!=0):
			a=archivo.cuentaMinus()
			print(a)
		else:
			print("El archivo no existe")
	elif n ==12:
		if(len(nombre)!=0):
			a=archivo.hexadecimal()
			print(a)
		else:
			print("El archivo no existe")
	elif n ==13:
		if(len(nombre)!=0):
			archivo.aMay()
		else:
			print("El archivo no existe")
	elif n ==14:
		if(len(nombre)!=0):
			archivo.aMin()
		else:
			print("El archivo no existe")
		