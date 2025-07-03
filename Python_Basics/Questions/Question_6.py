# Write a program which will take 3 inputs from the user and print them into acending order.

num1 = eval(input("Input First number: "))
num2 = eval(input("Input Second number: "))
num3 = eval(input("Input Third number: "))

if num1 > num2 and num1>num3:
    print(num1)
    if num2 > num3:
        print(num2)
        print(num3)
    elif num3 > num2:
        print(num3)
        print(num2)
elif num2 > num1 and num2>num3:
    print(num2)
    if num1 > num3:
        print(num1)
        print(num3)
    elif num3 > num1:
        print(num3)
        print(num1)
elif num3 > num1 and num3>num2:
    print(num3)
    if num2 > num1:
        print(num2)
        print(num1)
    elif num1 > num2:
        print(num1)
        print(num2)
