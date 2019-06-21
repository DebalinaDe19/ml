a= int(input("Enter the integer"))
b=[]

for i in range(2,a+1):
    if a%i ==0:
        b.append(i)


b.sort()

print("The smallest divisor is", b[0])
