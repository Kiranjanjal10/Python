email=input("Enter the email:")
passwrod=input("Enter the Password :")

if email=='kiran@gmail.com' and passwrod=='1234':
    print("Welcome")
elif email=='kiran@gmail.com' and passwrod != '1234':
    print('Incorrect password')
    passwrod=input("Enter password again:")
    if passwrod=='1234':
        print("welcome finally!!")
    else:
        print("Incorrect again!!!") 
else:
    print("Not correct")