number=int(input("Enter any number"))
sum1=0
cube=0
while(number!=0):
    digit=number%10

    cube=digit*digit*digit
    sum1= sum1+cube

    number= number/10


if(number==cube):
    print("Armstrong number")
else:
    print("Not an Armstrong")
