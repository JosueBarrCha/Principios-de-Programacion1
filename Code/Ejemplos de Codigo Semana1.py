#Costo de metro en Terreno
costo_metro = 0
ancho = 20
largo = 150
area = 0
monto = 0

costo_metro = float(input('Ingrese el costo del metro: '))
area = ancho * largo
monto = area * costo_metro

print('El monto a pagar es de: ', monto)



#Imprimir Fecha
import datetime

fecha_actual = datetime.datetime.now()
print(fecha_actual)



#Número mayor
primer_numero = 7
segundo_numero = 3
if primer_numero == segundo_numero:
    print('Ambos números son iguales')
else:
    if primer_numero > segundo_numero:
        print('El número mayor es: ', primer_numero)
    else:
        print('El número mayor es: ', segundo_numero)



#Imprimir nombre
nombre = ''
edad = 0
estatura = 0.0

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
estatura = float(input('Ingrese su estatura en metros: '))