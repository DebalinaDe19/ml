number=int(input("Enter the number to which the identity matrix would be printed"))

for item in range(1,number+1):
    for gem in range(1,number+1):

        if(item==gem):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()
            
