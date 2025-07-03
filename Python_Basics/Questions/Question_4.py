# Write a program which will take an number as an input from user and check weather the number is positive, negative or zero.

number = eval(input("Give any Number: "))

if number<0:
    print("The number is negative integer")
elif number==0:
    print("The number is neutral/zero")
else:
    print("The number is a positive integer")