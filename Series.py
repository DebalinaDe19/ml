number=int(input("Enter the limit of series"))
a=[]
for series in range(1,number+1):
    print(series,sep=" ",end=" ")
    if(series<number):
        print("+",sep=" ",end=" ")

    a.append(series)

print("=",sum(a))

   

