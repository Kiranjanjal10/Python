# Write a program to print the multiplication table of a number entered by the user.

number=int(input("Enter the table no :"))

for i in range(1,11):
    print(number,"X",i," :",i*number)