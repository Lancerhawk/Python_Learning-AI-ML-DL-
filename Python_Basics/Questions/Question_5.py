# 0 - 12 -> child, 13 - 19 -> teen, 20 - 45 -> Adult, 45 -> Elder

age = eval(input("Enter your Age: "))

if age<=12:
    print("You are a child, go play with toys.")
elif age<=19:
    print("You are a teen, go get a job")
elif age<=45:
    print("You are an adult, slow down son")
elif age>45:
    print("You are an elder, worthy of anyones respect")
else:
    print("invalid input son")