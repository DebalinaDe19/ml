a =int(input("Enter a number"))
count=0
while a!=0:
    digit=a%10
    count = count+1
    a=a//10

print(count)
