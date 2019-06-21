number=int(input("Enter a number"))

for i in range(1, number+1):
    a=[]
    for j in range(1,i+1):
        
        print(i,sep=" ",end=" ")
        if(i>j):
            print("+", sep=" ",end=" ")


        a.append(i)
        
    print("=", sum(a))
       

   
