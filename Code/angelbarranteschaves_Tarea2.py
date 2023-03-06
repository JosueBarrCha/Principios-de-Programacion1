#Bienvenida
#######################
import sys


print("BIENVENIDO AL SISTEMA DE RENOVACION DE LICENCIA DE CONDUCIR")
nombre=str(input("Por favor digite su nombre completo: "))

#requisitos de licencia
#######################

print(f"Bienvenido, {nombre}.Los requisitos para poder renovar su licencia de conducir son los siguientes:")
print("-Documento de identificacion al dia")
print("-Dictamen medico vigente")
print("-Multas de transito pagas")
print("-Menos de 12 puntos acumulados por infracciones de transito.")
print("Por favor digite cuidadosamente los siguientes datos para poder determinar su elegibilidad de renovacion de licencia:")

#Puntos acumulados
#######################

puntosacumulados=int(input("Por favor indique cuantos puntos ha acumulado:"))


#Estado de posibilidad de renovacion y tarifa
#############################################

if puntosacumulados >= 12:
    print(f"Usted ha acumulado {puntosacumulados} puntos.")
    print ("Su licencia se encuentra SUSPENDIDA.")
    print("Por acumular 12 o mas puntos en su licencia de conducir por infracciones de transito, no puede renovar su licencia en este momento.")
if puntosacumulados < 12:
    print(f"Usted ha acumulado {puntosacumulados} puntos.")
    print("Por haber acumulado menos de 12 puntos, usted se encuentra dentro de la posibilidad de renovar su licencia.")
    bcr=str(input("Esta usted realizando este tramite de renovacion en una agencia del Banco de Costa Rica?: Por favor digite si o no: "))
    bcrlower=bcr.lower()
    if puntosacumulados <4:
        tarifa=5000
        print(f"Por tener menos de 4 puntos acumulados, usted debe pagar un monto de ₡{tarifa} colones")
        print("Una vez renovada su licencia, su periodo de vigencia es de 6 annos.")
    if puntosacumulados in [5,6,7,8]: #Se utilizan listas para poder tener el rango de puntos que determinan cada tarifa y vigencia de la licencia
        tarifa=10000
        print(f"Por tener entre 5 y 8 puntos acumulados, usted debe pagar un monto de ₡{tarifa} colones")
        print("Una vez renovada su licencia, su periodo de vigencia es de 4 annos.")
    if puntosacumulados in [9,10,11]:
        tarifa=10000
        print(f"Por tener entre 9 y 11 puntos acumulados, usted debe pagar un monto de ₡{tarifa} colones")
        print("Una vez renovada su licencia, su periodo de vigencia es de 3 annos.")
    if bcrlower== "si":
        tarifabcr=4200
        print(f"Por realizar el tramite en una agencia BCR. debe cancelar una tarifa de ₡{tarifabcr}")
        preciofinal=tarifa+tarifabcr
        print(f"El monto total a cancelar por la renovacion de su licencia es de ₡{preciofinal} colones.")
    else:
        preciofinal=tarifa
        print(f"El monto total a cancelar por la renovacion de su licencia es de ₡{preciofinal} colones.")

#Cerrar programa
################

cerrarprograma=str(input("Por favor verifique que todos los datos esten correctos y proceda a presionar cualquier tecla para cerrar el programa."))