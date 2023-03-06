d = int(input())
m = int (input())
a = int (input())

dias31=[1,3,5,7,8,10,12]

if d==31 and m==12:
    d=1
    m=1
    a=a+1
elif (m in dias31) and d==31:
    d=1
    m=m+1
elif (m not in dias31):
    d=1
    m=m+1
elif d<31:
    d=d+1
else:
    print("nel pastel")
print (f"manana es {d}/{m}/{a}")

