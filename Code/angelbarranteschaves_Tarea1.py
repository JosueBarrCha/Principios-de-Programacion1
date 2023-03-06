salario_mensual = float(input("Por favor indicar su salario mensual:"))

salario_pendiente = float(input("Tiene usted algun salario pendiente?"))

vacaciones = int(input("Digite su saldo actual de vacaciones:"))

monto_por_vacaciones = (salario_mensual/30) * vacaciones

aguinaldo_proporcional = salario_mensual/12

preaviso = salario_mensual

antiguedad = int(input("Cuántos años tiene de trabajar en la empresa?"))

cesantia = (salario_mensual/30)*20 * antiguedad

#se imprime este grupo de datos para que el usuario pueda revisar en caso de haber cometido algun error en la entrada
print ("Salario mensual: ₡", salario_mensual)
print ("Salario Pendiente: ₡", salario_pendiente)
print("Su saldo actual de vacaciones disponibles es de:", vacaciones)
print("Monto por vacaciones:₡", monto_por_vacaciones)
print ("Aguinaldo proporcional: ₡", aguinaldo_proporcional)
print ("Su monto por cesantía es: ₡", cesantia)

liquidación = (salario_pendiente + monto_por_vacaciones + aguinaldo_proporcional + preaviso + cesantia)

#se utilizan dos lineas diferentes por razones esteticas
print ("El monto de su liquidación es el siguiente:")
print ("₡",round(liquidación))