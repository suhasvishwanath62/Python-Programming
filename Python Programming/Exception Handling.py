a = 23456
b = 23
try:
    print("Resource open")
    print(a/b)
except Exception:
    print("you cannot divide by zero")

finally:
    print("Resource close")

