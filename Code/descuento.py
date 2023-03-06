noches = int(input("cuantas noches planea quedarse?"))
costo_noche=float(input("cual es el costo de la estadia por noche?"))
if (noches > 4):
    descuento=0.15
else:
    descuento=0
descuento= (costo_noche*descuento)

subtotal=costo_noche- descuento
print (subtotal)
print (descuento)
total=subtotal-descuento
print ("su precio final es de", total)