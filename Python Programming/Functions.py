def greet(name):
    print(f"Hello, {name}")
greet("suhas")

print("-------------------------------------------------")

def calculate_area(length,breath):
    area = length * breath
    return area
area = calculate_area(10,20)
print(f"Area: {area}")

print("-------------------------------------------------")

def add_numbers(a,b):
    add = a + b
    return add
add = add_numbers(10,45)
print(f"10 + 45= {add}")

print("-------------------------------------------------")

def employee_details(name,job):
    print(f"Name: {name}")
    print(f"Job: {job}")
employee_details(name="Suhas",job="Engineer")

print("-------------------------------------------------")

def intro(name="BMW"):
    print(f"Name: {name}")
intro() # prints Default Parameters
intro("AUDI")

print("-------------------------------------------------")

def arguments(*args,**kwargs):
    print(f"positional arguments: {args}")
    print(f"keyword arguments: {kwargs}")
arguments("suhas","Engineer",Login="time",Logout="notime")

print("-------------------------------------------------")

# Returning Values

def multiply(a,b):
    return a * b
mul = multiply(12,45)
print(mul)

print("-------------------------------------------------")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

print("--------------------------------------------------")

def local_variable_example():
    x = 10  # Local variable
    print(x)

local_variable_example()
# print(x)  # Raises NameError no variable 'x' defined.

print("--------------------------------------------------")

def calculate_sum():
    a = 10
    b = 34
    sum = a + b
    return sum
print(calculate_sum())

print("--------------------------------------------------")

# Recursive Functions

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(21))

print("--------------------------------------------------")

def odd():
    print("Odd numbers:")
    for i in range(1,11,2):
        print(i,end=" ") # prints all numbers of odd
    print() # moves the cursor to next line after printing all numbers.

def even():
    print("even numbers:")
    for j in range(2,11,2):
        print(j,end=" ")# prints all numbers of even
    print() # moves the cursor to next line after printing all numbers.
odd()
even()

print("--------------------------------------------------")

def odd_num(n):
    num = 1
    while num <= n:
        print(num)
        num += 2
odd_num(20)

print("--------------------------------------------------")

def div_num(a,b):
    if a < b:
        a,b = b,a # Swapping the numbers.
    print(a/b)
div_num(2,3)

print("--------------------------------------------------")

# Lambda Functions

f = lambda a,b : a+b
result = f(5,6)
print(result)




