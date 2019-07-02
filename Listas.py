#Nombre: listas.py

lista=[]

def agregaItem(dato):
	lista.append(dato)


def eliminarItem(dato):
	
		if (dato in lista):
			lista.remove(dato)
			print("Dato eliminado")
		else:
			print("No se encontro el item en la lista")
		
		

def imprimirLista():
	j=0
	for i in lista:
		print("Item: ",j,",", i)
		j=j+1



def main():
	print("--Scrip para trabajar con listas---")
	print("1.- Agregar elementos a la lista")
	print("2.- Buscar elemento en la lista")
	print("3.- Modificar un elemento en la lista")
	print("4.- Eliminar un elemento de la lista")
	print("5.- Imprimir elementos de la lista")
	print("6.- Salir")
	opc = int(input("Elegir opción"))
	if (opc==1):
		Item = input("Introduce el valor del elemento : ")
		agregaItem(Item)
	elif(opc==2):
		print("Opcion 2")

	elif(opc==3):
		print("Opcion 3")

	elif(opc==4):
		da = input("Dato que quiere eliminar : ")
		eliminarItem(da)	

	elif(opc==5):
		imprimirLista()	
	

	elif(opc==6):
		print("Fin del programa")

	



	if __name__ == '__main__':
		main()

		


