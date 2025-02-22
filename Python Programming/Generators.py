def square_ten(n):
    return n * n
value = square_ten(21)
print(value)

print("--------------------------------------------")

# Generators:
def square_tenn():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1
values = square_tenn()
for i in values:
    print(i)

print("--------------------------------------------")

def triseq(n):
    s = 0
    for i in range(1,n+1):
        s += i
        i += 1
        yield s
for x in triseq(5):
    print(x)

print("--------------------------------------------")

def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
for i in gen:
    print(i)

