'''
EJERCICIO 1
#Determinar si una persona tiene fiebre. Una persona tiene fiebre si la temperatura es mayor a 37 grados. El programa recibe como información la temperatura de la persona.

temperatura = float(input("Por favor indique su temperatura corporal actual:"))
if temperatura > 37:
    print(f"Su temperatura actual es de {temperatura}°C. Usted tiene fiebre.")
else:
    print (f"Su temperatura actual es de {temperatura}°C. Usted NO tiene fiebre.")



#EJERCICIO 2
#Determinar si un ciudadano puede votar. Un ciudadano puede votar si ya cuenta con 18 annos cumplidos. El programa recibe la edad del ciudadano.

edad=int(input("Por favor indique su edad actual:"))
if edad >= 18:
    print("Usted SI tiene la edad para ejercer su derecho a voto.")
else: 
    print(f"Su edad actual es de {edad} annos. Usted NO puede ejercer su derecho al voto")




#EJERCICIO 3
#Determinar si un estudiante gano o perdio un curso, si pierden el curso todos los estudiantes cuya nota es menor a 70

estudiante=str(input("Por favor indique el nombre del estudiante:"))
nota=int(input(f"Por favor introduzca la nota de {estudiante}:"))
if nota >=70:
    print(f"{estudiante} ha APROBADO el curso con una calificacion de {nota}.")
else:
    print(f"{estudiante} ha REPROBADO el curso con una calificacion de {nota}. La nota minima para aprobarlo debe ser de al menos un 70.")


#EJERCICIO 4
#Costa Rica tiene las fronteras cerradas para todas personas que provienen del exterior debido a la pandemia, salvo aquellas cuya nacionalidad es costarricense. El programa recibe como entrada la nacionalidad de la persona.


tico=str("costarricense")

nacionalidad=str(input("Por favor introduzca la nacionalidad de la persona:"))
if nacionalidad == tico:
    print("Acceso a Costa Rica APROBADO.")
else:
    print("Acceso a Costa Rica DENEGADO.")



#EJERCICIO 5
#Definir si una persona debe pagar impuesto al valor agregado por su consumo mensual de electricidad. El programa recibe el consumo mensual de la persona. Se deduce un impuesto del 13% si el consumo es mayor a 200 kWh.

consumomensual=int(input("Por favor indique su consumo de electricidad del presente mes:"))
if consumomensual > 200:
    impuesto=consumomensual*1.13
    print(f"Su consumo mensual fue de {consumomensual}KWh.")
    print("Al ser su consumo mensual MAYOR de 200KWh, se le aplica a su tarifa un impuesto del 13%.")
elif consumomensual < 200:
    print("Al ser su consumo mensual MENOR de 200KWh, NO se aplica impuesto.")

'''

#EJERCICIO 6
#El Gobierno ha decidido que todas aquellas personas que tienen un salario igual a superior a un millón de colones deben pagar un impuesto del 10%. Calcule el salario neto de un trabajador. El sistema recibe el salario del trabajador como entrada

salariobruto=int(input("Por favor indique su salario:"))
if salariobruto >= 1000000:
    salarioneto=1000000*0.9
    print(f"Su salario neto es de c{salarioneto}. Se le ha aplicado un impuesto de 10% al superar el millon de colones.")
else:
    salarioneto=salariobruto
    print(f"Su salario neto es de c{salarioneto}.")

