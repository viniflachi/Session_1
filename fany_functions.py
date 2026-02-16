def add_numbers(a, b, c=0):
    return a + b + c

add_numbers(1, 2)
print(add_numbers(5, 8))
print(add_numbers(5, 8, 3)) #call by position
print(add_numbers(b = 7, c = 11, a = -100)) #call by name

#a funtion that alls itself is alled factorial of n-1
def factorial (n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(20))

#functions can call other functions
#th nam is bond, james bond
def greeting(name):
    message = f"The name is {name}\n"
    message += (f"Je m'appelle: Le{name}")
    return message
    return f"The name is: {name}"

def bond_name(first, last):
    return f"{last} {first}{last}"

print(greeting("Sanchez, Maria Sanchez"))
print(bond_name("Jerry", "Bond"))