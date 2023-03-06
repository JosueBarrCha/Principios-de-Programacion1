"""
#hay patrones que hace que redactar el codigo se vuelva repetitivo. Ej con area de cuadrado:
lado=4
area=lado*lado
#si quisieramos hacer ese programa varias veces habria nada mas que cambiar el valor de lado

#caso con un menu
print("******************")
print("Hola Programadores")
print("opcion 1 fotos")
print("Opcion 2 videos")
print("******************")
#ley de programacion: dont repeat yourself. para no tener que poner eso varias veces

# def modulariza el codigo, y genera funciones
def menu():
    print("******************")
    print("Hola Programadores")
    print("opcion 1 fotos")
    print("Opcion 2 videos")
    print("******************")
#Una vez queda modularizada, para invocar esa funcion nada mas se pone 'nombre()'
#Solo se pondria de la siguiente manera para invocar el
menu()

#para definir el calculo de area
def areaCuadrado(lado): #el lado es un PARAMETRO
    area=lado*lado
    return area
area=areaCuadrado(5)
print(area)

menu()
#lado=int(input("digite la medida del lado: "))
#return da un valor a la funcion, aunque NO SIEMPRE tiene un return, no siempre hay que asignarle un valor
lado=int(input())
area=areaCuadrado(lado)
print(area)

#Crear una funcion que retorne la suma de dos parametros
no1=int(input("Digite un numero:"))
no2=int(input("Digite otro numero:"))

def suma(no1,no2):
    return no1+no2

print (suma(no1,no2))


#funcion de menu
def mostrarmenu():
    print("******************")
    print("Hola Programadores")
    print("opcion 1 fotos")
    print("Opcion 2 videos")
    print("******************")

#esta pide un dato de un imput y lo retorna
def leeropcion():
    opcion=int(input("Seleccione una opcion:"))
    print()
    return opcion


def accion1():
    pass#el algoritmo para realizar la accion 1
def accion2():
    pass#el algoritmo para realizar la accion 2
def accion3():
    pass#el algoritmo para realizar la accion 3
def accion4():
    pass#el algoritmo para realizar la accion 4

def menu():
    continuar=True
    ehile continuar==True

"""
def poneguion(palabra):
    resultado=""
    for letra in palabra:
        resultado=resultado+"-"
    return resultado

def encuentraLetra(palabra_original,palabra_parcial,letra_nueva):#palabra_parcial contiene las letras que ya se han logrado encontrar
    subpalabra=""
    for indice, letra in enumerate(palabra_original):
        if letra==letra_nueva:
            subpalabra=subpalabra+letra_nueva
        else:
            subpalabra=subpalabra+palabra_parcial[indice]
    return subpalabra

def ahorcado(palabra_secreta):
    letra=input()
    palabra_parcial=poneguion(palabra_secreta)
    if letra in palabra_secreta:
        palabra_parcial=encuentraLetra(palabra_secreta, palabra_parcial, letra_nueva)
        print(palabra_parcial)
    else:
        print("jale bateador")

ahorcado("papaya")


# b=True
# palabra_secreta=input()
# cont=0
# while b==true:
