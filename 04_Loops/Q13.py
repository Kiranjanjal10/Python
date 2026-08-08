# Write a program to count the number of digits in an integer using a while loop.

integer=int(input("Enter the Integer :"))

count=0
while(integer > 0):
    integer//=10
    count +=1
print("No of Digit in Number is :",count)