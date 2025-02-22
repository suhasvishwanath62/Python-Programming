x = True
y = True
result = x and y
print(f"The x and y are:",result)

x = False
y = True
result = x or y
print(result)

x = True
result = not x
print(result)

x = 10
y = 5
z = 20
result = (x > y) and (z > x)
print(result)

x = 10
y = 5
z = 20
result = (x > y) or (y > x)
print(result)

