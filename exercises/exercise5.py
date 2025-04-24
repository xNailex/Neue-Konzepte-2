def greet_user(name):
    return f"Hello, {name}!"

def is_even(number):
    return number % 2 == 0

print(greet_user(input("Please enter your name:")))
print(is_even(int(input("Please enter a number:"))))