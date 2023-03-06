#Para imprimir una secuencia de numeros, por ejemplo
"""
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)


#Utilizando iteraciones

numero=0 #porque 0 es el primer numero
while numero<3000000: #el numero<3000000 se llama EVAL, o evaluacion, porque evalua
    print(numero)
    numero=numero+1 #esta parte se llama MODIFICACION porque modifica la variable de la evaluacion
    #otra manera de escribir la modificacion seria con numero+=1
    

edad=int(input("Edad: "))

while edad<0 or edad>200:
    edad=int(input("Edad: "))
    

edad=input("Edad: ")

while not edad.isnumeric():
    edad=int(input("Edad: "))
edad=int(edad)
print(f"edad is {edad}")



listanumeral=[1,2,3,4,5,6,7,8,9,1,10,211,7]
total=listanumeral[0]+listanumeral[1]+listanumeral[2]+listanumeral[3]+listanumeral[4]+listanumeral[5] #se hace bastante largo porque la lista puede ser mucho mas larga
print(total)
#Se puede usar el SUM tambien:



listanumeral=[1,2,3,4,5,6,7,8,9,1,10,211,7]
#para sumar los numeros uno auno con un while, para nmo tener que cambiar el codigo cada vez que cambie la lista. 
#el len() da la cantidad de elementos que tiene una lista
len(listanumeral)
print(len(listanumeral))
#Va a darme el total de la lista, que tiene 13 elementos. 
"""

#Con una lista que tiene listas dentro
listanumeral=[1,2,3,4,5,6,7,8,9,1,10,211,7]
x1=[[1,2,3],[8]]
len(x1[0])
print(len(x1[0]))

pos=0
while pos<len(listanumeral):
    print(listanumeral[pos])
    pos=pos+1
#El pos en este caso es el que indica el indice para escoger un elemento

#acumulador
pos=0
acumulador=0
while pos<len(listanumeral):
    print(listanumeral[pos])
    acumulador=acumulador+listanumeral[pos]
    pos=pos+1

print (acumulador)