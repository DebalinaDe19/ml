alphabet=int(input("Enter the character to which the pattern will be printed in ASCII"))


for item in range(65,alphabet):
    for gem in range(65,item):
        ch=chr(alphabet)


        print(ch,sep=" ",end=" ")

    print()
