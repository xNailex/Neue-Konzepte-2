age = input("Please enter your age:")

age = int(age)
if age < 0:
    print("Age cannot be negative.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")