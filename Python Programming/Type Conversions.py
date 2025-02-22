age = 21
height = 5.5
print(f"My age is "+ str(age)+" and height is "+str(5.5))

salary = 35000.00
print(int(salary))

cars = ["BMW","AUDI","TOYOTA"]
tuples = tuple(cars)
print(tuples)

invalid_str = "kishan"
try:
    num = int(invalid_str)
except ValueError:
    print(f"Cannot convert '{invalid_str}' to integer")

salary_t = "55600.50"
print(f"The total CTC is",float(salary_t))




