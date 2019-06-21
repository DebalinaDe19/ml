a =int(input("Enter a number"))
rev=0
while a!=0:
    digit=a%10
    rev=rev*10+digit
    a=a//10

    if rev==a:
        print("PAlindrome number")
    else:
        print("Not a palindrome number")
    

