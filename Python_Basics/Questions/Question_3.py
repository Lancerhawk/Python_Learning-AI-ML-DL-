#Write a program which will take age as an Input from the user and print if the user can vote or not.

age = eval(input("Enter your Age: "))

if age>=18 | age<100:
    print("You can Legally Vote.")
elif age>100:
    print("You CAN Vote, but you should be dead either way till the next elections.")
else:
    print("You can't vote legally, use illegal way called baap ka paisa.")