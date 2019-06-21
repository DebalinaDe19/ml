mathematics= int(input("Enter the marks of maths"))
science= int(input("Enter the marks of science"))
english= int(input("Enter the marks of english"))
history= int(input("Enter the marks of history"))
geography= int(input("Enter the marks of geography"))

avg=(mathematics+science+english+history+geography)/5
if avg>90 and mathematics>85:
    print("Grade A")

elif (avg<= 89 and avg>= 75):
    print ("Grade B")


elif( avg <=74 and avg >= 50):
    print (" Grade C")

else:
    print("fail")
