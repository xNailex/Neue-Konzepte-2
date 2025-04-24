input1 = input("Please enter the first number:")
a = int(input1)
input2 = input("Please enter the second number:")
b = int(input2)

print(f"{a}, {b}")
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b}")
print(f"Integer Division: {a // b}")
print(f"Remainder: {a % b}")
print(f"Exponent: {a ** b}")

print(f"Equal: {a == b}")
print(f"Not Equal: {a != b}")
print(f"Less Than: {a < b}")
print(f"Greater Than: {a > b}")
print(f"Less Than or Equal: {a <= b}")
print(f"Greater Than or Equal: {a >= b}")

print(f"Are both numbers positive? {a > 0 and b > 0}")
print(f"Is at least one number positive? {a > 0 or b > 0}")
print(f"Is at least one number positive? {a < 0 or b < 0}")

a+=1
print(f"{a}")
