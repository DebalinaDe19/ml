a= int(input("Enter the number for variable a"))
b= int(input("Enter the number for variable b"))
c =int(input("Enter the number for variable c"))

d=[]
d.append(a)
d.append(b)
d.append(c)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):


            if(i != j&j != k&k != i):
                print(d[i], d[j], d[k])
                
       
