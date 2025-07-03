#Write a program which will take input from user and check if the number is divisible by 3 then it will print fizz, 

number = eval(input("Enter the number: "))

if number%3 == 0 and number%5 == 0:
    print("fizz")
elif number%5 == 0:
    print("Buzz")
elif number%3 == 0:
    print("Fizz and Buzz")
else:
    print("Not found")