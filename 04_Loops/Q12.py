# Write a program to calculate the factorial of a number using a for loop.

number=int(input("Enter the number :"))
factorial=1
for i in range(1,number+1):
    factorial=factorial*i
print("Factorial of number ",number," is :",factorial)