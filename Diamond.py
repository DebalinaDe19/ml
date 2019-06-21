n= int(input("Enter the number of rows"))

for item in range (0,n+1,1):
    for  gem in range (n,item,-1):
        print(" ",sep=" ",end=" ")

    for kin in range(0,item):
        print("* ",sep=" ",end=" ")

    print()
for item in range (0,n+1,1):
    for  gem in range (0,item,1):
        print(" ",sep=" ",end=" ")

    for kin in range(n,item,-1):
        print("* ",sep=" ",end=" ")

    print()
