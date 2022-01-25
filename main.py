import random


pass12 = 25


a1 = input("enter your name:-")

a = 0
while a < 6:

    print("Welcome", a1)

    a = a+1

    a2 = int(input("enter your password"))

    if a2 == pass12:

        print("1. adition")

        print("2. subtraction")

        print("3. multiplication")

        print("4. divide")

        choice=input("enter you choice:-")
        num1= int(input("Enter number1 0_0:-"))
        num2= int(input("Enter number2 0_0:-"))
    if choice ==  "1":
        print(num1,"+", num2,"=",(num1+num2))
    elif choice == "2":
        print(num1,"-", num2,"=",(num1-num2))
    elif choice == "3":    
        print(num1,"*", num2,"=",(num1*num2))
    elif choice == "4":
        print(num1,"/", num2,"=",(num1/num2))
    else:

        print("wrong password")
        exit()

    
