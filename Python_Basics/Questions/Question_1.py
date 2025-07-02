#Write an program, which will take length and breath as an input of an rectangle and calculate the Area and Parameter of it.

length = eval(input("Enter the length of the Rectangle: "))
breath = eval(input("Enter the breath of the Rectangle: "))

area = length * breath
parameter = 2 * (length + breath)

print("The Area of the rectangle is:",area)
print("The Parameter of the rectangle is:",parameter)