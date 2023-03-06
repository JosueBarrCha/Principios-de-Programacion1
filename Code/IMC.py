nombre = input("ingrese el nombre compa ")
estatura = float(input ("ingrese la estatura pls "))
peso = float(input("ingrese que tan gordo esta "))

imc = peso / (estatura**2)

#creo una variable mensaje, que me imprime eso. el imc se convierte en string porque solo se puede unir un string con otro string!

msj = "saludos "+nombre+" su imc es de:"+str(imc)

#otra manera de hacerlo seria la siguiente
    #msj= f"saludos, {nombre} su imc es de: {imc}
    #el fstring da formato a la variable y tambien convierte los valores en string

print(msj)