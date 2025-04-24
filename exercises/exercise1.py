a = 10 #int
b = 3.14 #float
c = "Hello" #str
d = True #bool
e = [1, 2, 3] #list
f = (1, 2, 3) #tuple
g = {1: "one", 2: "two", 3: "three"} #dict
h = {1, 2, 3} #set

print(f"Integer: {a}")
print(f"Float: {b}")
print(f"String: {c}")
print(f"Boolean: {d}")
print(f"List: {e}")
print(f"Tuple: {f}")
print(f"Dictionary: {g}")
print(f"Set: {h}")
print(f"Type of a: {type(a)}")
print(f"Type of b: {type(b)}")
print(f"Type of c: {type(c)}")
print(f"Type of d: {type(d)}")
print(f"Type of e: {type(e)}")
print(f"Type of f: {type(f)}")
print(f"Type of g: {type(g)}")
print(f"Type of h: {type(h)}")

input = input("Please enter a number:")
print(f"You entered: {int(input)}")
print(f"You entered: {type(int((input)))}")
print(f"You entered: {float(input)}")
print(f"You entered: {type(float((input)))}")