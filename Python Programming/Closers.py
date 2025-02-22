def adder(value):
    def inner_function(base):
        return base + value
    return inner_function
adder_5 = adder(5)
result = adder_5(10)
print(result)

