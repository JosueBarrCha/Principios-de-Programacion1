"""
#EJERCICIO 1

# Calcular el precio final de cualquier producto, si se sabe que la tasa de impuesto al valor agregado es de un 13 %. El algoritmo debe recibir el nombre del producto y el precio, y debe imprimir el nombre del producto y el precio final. Para los efectos del ejercicio, TODOS los productos pagan impuesto.


impuesto = 0.13
producto = str(input("Por favor inserte el nombre del producto:" ))


precio_subtotal = float(input("Por favor inserte el precio del producto:"))



Impuesto_a_Pagar = precio_subtotal * impuesto
Precio_final = precio_subtotal + Impuesto_a_Pagar

print ("Producto: ", producto)
print ("Precio: ₡",precio_subtotal)
print ("Impuesto a Pagar: ₡",Impuesto_a_Pagar)
print ("El precio final a pagar por su compra es de: ₡",Precio_final)

Cerrar = str(input("Por favor verifique que la cantidad sea la correcta y presiona cualquier tecla para cerrar el programa"))



#EJERCICIO 2

#Calcular la cantidad de kilómetros de un viaje realizado en carro. El algoritmo debe recibir el kilometraje del vehículo antes de iniciar el viaje, y el kilometraje del vehículo al terminar el viaje. Se debe imprimir el total de kilómetros del viaje

kilometraje_anterior = int(input("Por favor indique el kilometraje antes del viaje: "))

print (f"Kilometraje anterior al viaje es de: {kilometraje_anterior} km")

kilometraje_posterior = int(input("Por favor indique el kilometraje despues del viaje: "))

print (f"Kilometraje anterior al viaje es de: {kilometraje_posterior} km")

distancia_viajada = kilometraje_posterior - kilometraje_anterior

print (f"La distancia total viajada fue de {distancia_viajada} km.")

Cerrar = str(input("Por favor verifique que la cantidad sea la correcta y presiona cualquier tecla para cerrar el programa"))

"""


#EJERCICIO 3

#Encontrar la edad de Ana dentro de diez años, si la edad de Ana es dos veces la edad de Elena. El programa recibe como entrada la edad actual de Elena, y debe imprimir la edad de Ana dentro de diez años.

edad_elena = int(input("Digite la edad actual de Elena: "))
edad_ana_diez_annos = (2*edad_elena)
print (edad_ana_diez_annos)