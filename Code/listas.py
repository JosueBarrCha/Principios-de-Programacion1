#Ese elemento me va a imprimir "hola" porque ese string se encuentra en la posicion numero 2 de la lista. 
l=[8,3,"hola", [1,2], 5, 6.3]
l[2]

#Con los elementos de la lista tambien se puede hacer operaciones matematicas. 

op=(l[0] + l[1])
print (op)

#Esta operacion me va a dar 11 porque esta sumando 8 + 3

op2= l[l[3][0]+l[l[3][0]]]
print(op2)

m = [[0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]]

op3=m[0][2]=1
#lo que hago ahi arriba es asignarle un valor de 1 a la posicion 2 de la posicion 0 de lista m
print(m)

#Que tipo de dato es m? es un class "list", independientemente del tipo de datos que almacene la lista. 
#Para imprimir la inicial de mi nombre


def imprimeMatriz(matrix): # 2+n**2 
    result=""
    for i in matrix:
        for j in i:
            result+=str(j)+"\t"
        result+="\n"
    return result
print(imprimeMatriz(m))

