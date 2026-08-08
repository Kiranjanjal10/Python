# Write a program to find the largest of three numbers using if-elif-else.

a=int(input("Enter first No :"))
b=int(input("Enter second No :"))
c=int(input("Enter third No :"))

if a<b and a<c:
    print("Smallest is :",a)
elif b<c:
    print("Smallest is :",b)
else:
    print("Smallest is :",c)