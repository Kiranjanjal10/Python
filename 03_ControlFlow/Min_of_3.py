a=int(input("First Num :"))
b=int(input("Second Num :"))
c=int(input("Third Num :"))

if a<b and a<c:
    print("Smallest is :",a)
elif b<c:
    print("Smallest is :",b)
else:
    print("Smallest is :",c)