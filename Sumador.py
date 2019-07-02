#Sumar 2 numeros 

def suma(num1,num2):
    return num1+num2


def multiplica(num1,num2):
    return num1+num2


def divide(num1,num2):
    return num1/num2
#Comparar numeros
def compara(num1,num2):
    if(num1>num2):
        print("El numero mayor es el No1: ",num1)
        
    elif(num2>num1):
        print("El mayor es el num2: ",num2)
        
    else:
        print(" Los numeros son iguales")
        
        
    
def main():
    print ("Operaciones basicas con numeros enteros")
    print("\n")
    n1 = int( input("Introduce el primer numero"))
    n2 = int( input("Introduce el segundo numero"))
 
    print("La suma es: ",str(suma(n1, n2)))
    print("La multiplicacion es:",str(multiplica(n1, n2)))
    print("La division es:", str(divide(n1, n2)))
if _name_ == "_main_":
    main()