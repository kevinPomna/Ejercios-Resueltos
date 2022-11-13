#Ejercicios resueltos de tarea
#Autor: Kevin Poma
'''
#Ejercicio 1:
#Multiplicar 2 números sin usar el símbolo de la multiplicación

num1=int(input("Ingresa un numero -> "))
num2=int(input("Ingresa un numero -> "))
num3= 0

for i in range(num2):
    num3=num3+num1
print(num3)

#Ejercicio 2  Ingresar nombre y appelido e imprimelo al reves

nombre = input("Ingresa tu nombre y apellido: ")
reversed_String =''.join(reversed(nombre))
print(reversed_String)

#Ejercicio 3 crear una un script que encuentre el numero el elemnto menor a una lista 
lista=[0,1,2,3,4,8,6,7]

def menor (lista):
    min = lista[0]
    for x in lista:
        if x < min:
            min = x
            return min

def main(lista):
    print ("La lista es ", lista)    
    print ("El número menos es: ", min(lista))
 
main(lista)

#Ejercicio 4 Crear un scrip que imprima el volumen de una esfera por su radio 
radio = float(input("ingresa el radio de tu esfera: " ))
radio2 = (4*3.14) *(radio**3)/3
print(radio2,"m^3")

#Ejercicio 5 Crear un scrip que indique si el usuario es mayor de edad
edad = int(input("Ingresa tu edad: "))

if edad>18 :
    print("Usted usuario es mayor de edad")
else:
         print("Usted usuario es menor de edad")    

#Ejercicio 6 Crear un scrip que me permita calcular si un numero es par o impar

num = int(input("ingrese un numero: "))
num2 = num % 2

if num2 == 0:
   print("Tu numero es par")
else:
    print("Tu numero es impar")    

# Ejercicio 7 Crear un scrip que indique cuantas vocales tiene un palabra

def contar_vocales(vocales):
    voc = 0
    for c in vocales:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
            voc=voc+1
    return voc

vocales = input('Ingresa una palabra: ')
print (contar_vocales(vocales))

#Ejercicio 8 Crear un script que reciba una cantidad infinita de numeros hasta decir basta, luego que imprima la suma de los numeros ingresadas,
ciclo = int(input("Ingresa el numeros de veces que desees ingresar numeros: "))
num3 = 0
num2 = 0
while num2<ciclo:
    num2+=1
    num1 = int(input("Ingresa tus numero: ",))   
    num3 = num1+num3 
    num4 = num3
    if num2>ciclo-1:
       print("La suma de tus numeros ingresados es igual:",num4)
   
#Ejercicio 9

cal=float(input("ingrese su calificacion: "))

if cal>=9 and cal <= 10:
    print(f"{cal:} A")
elif cal>=8 and cal<9:
    print(f"{cal:} B")
elif cal>=7 and cal<8:
    print(f"{cal:} C")
elif cal>=6 and cal<7:
    print(f"{cal:} D")
elif cal>=0 and cal<6:
    print(f"{cal:} F")
else:
    print("Valor Desconocido")               

#Ejercicio 10

num= [1,2,3,4,5]
num.sort(reverse=True)
num2 = num
print(num2)

#Ejercicio 11
num1 = 6
while num1 >= 1:
    num1-=1
    print(num1)


#Ejercicio 12
alto = int(input("Ingrese el alto del rectangulo: ")) 
ancho = int(input("Ingrese el ancho del rectangulo: ")) 
area = alto*ancho
perimetro = alto+ancho
print(f"Area del rectangulo es= {area} ")
print(f"Perimetro del rectangulo es= {perimetro} ")

#Ejercicio 13

num = 0
while num<=10:
    num+=1
    if num%3 == 0:
        print(f"Numeros divisibles entre 3: '{num}'")

#ejercicio 14

autor = "Enrique Barrios"
titulo = "Ami el niño de las estrellas"
print(f"Libro: {titulo} , autor: {autor}")

#Ejercicio 15
num1 = int(input("Ingrese su primer numero: "))
num2 = int(input("Ingrese su segundo numero: "))
print(f"Su primer numero es: {num1}")
print(f"Su segundo numero es: {num2}")
if num1>num2:
    print(f"El numero  mayor es: {num1}")
else:
    print(f"El numero mayor es: {num2}")

#Ejercicio 16

tupla = (13, 1, 8, 3, 2, 5, 8)
new_list=[]
for x in tupla:
    if x < 5:
       new_list.append(x)
       print(new_list)

#Ejercicio 17 

num = int(input("Ingresa un numero: "))
potencia = int(input("Ingresa la potencia: "))
res = num**potencia
print(f"Tu resultado es = {res}")

#Ejercicio 18

num1= int(input("Ingresa un numero: "))
num2=int(input("Ingresa otro numero: "))
res = num1+ num2
print(f"La suma es= {res}")

#Ejercicio 19
a = int(input("Ingresa un numero de cuatro digitos: "))
b = int((a%100)/10)
c4 =a % 10
c3 = int((a % 100) / 10)
c2 = int((a % 1000) / 100)
cl = int((a - (a % 1000)) / 1000)
print(str(c4)+str(c3)+str(c2)+str(cl))

#Ejercicio 20
 
def saludo(nombre):
     print(f"Hola mi nombre es {nombre} un gusto en conocerte.")

saludo("Kevin")
''' 