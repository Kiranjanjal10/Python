# Write a program to calculate a student's grade:
# 90–100 → A
# 75–89  → B
# 60–74  → C
# 40–59  → D
# Below 40 → F

marks=int(input("Enter the marks :"))

if marks<=100 and marks>=90:
    print("Grade A")
elif marks<=89 and marks>=75:
    print("Grade B")
elif marks<=74 and marks>=60:
    print("Grade C")
elif marks<=59 and marks>=40:
    print("Grade D")
else:
    print("Grade F")