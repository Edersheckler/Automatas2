import math as mat

#---------------------
# funcion para calcular area
#--------------------------

def calcularArea(r):
	area = mat.pi*(mat.pow(r,2))
	return area

def calcularDiametro(d):
	diam = d*2
	return diam

def main():
	ciclo = True
	while ciclo == True:
		print ('Script para calcular area de circunferencia')
		radio = float (input ('Introduce el valor del radio: '))
		# Invocar los metodos
		print ('El area es: ',calcularArea(radio))
		print ('El diamtro es: ',calcularDiametro(radio))

		resp = input ("Desea hacer otro calculo: (s/n)?")
		if (resp == 's' or resp == 'S'):
			ciclo = True
		else:
			ciclo = False
	else:
		print("Fin del programa..")


if _name_ == "_main_":
	main()