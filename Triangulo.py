#-------------------------------
# Funcion para identificar el tipo del triangulo
#-------------------------------

def identifica(l1,l2,l3):
	#Equilatero
	if(l1 == l2 and l2 == l3):
		print ("El triangulo es equilatero: ",l1,' , ',l2,' , ',l3,'.')
	#Isoceles son dos lados iguales
	elif(l2 != l3 and l1 != l3 and l1!=l2):
		print ("El triangulo es escaleno: ",l1,' , ',l2,' , ',l3,'.')
	#Escaleno son sus lados diferentes
	else:
		print ("El triangulo es Isoceles: ",l1,' , ',l2,' , ',l3,'.')
	print ("El perimetro es: ",(l1+l2+l3))



def main():
	print ("----- Scrpit para identificar triangulos -----")
	lado1 = float(input("Introduce el lado 1: "))
	lado2 = float(input("Introduce el lado 2: "))
	lado3 = float(input("Introduce el lado 3: "))
	identifica(lado1,lado2,lado3)

if __name__ == "__main__":
	main()