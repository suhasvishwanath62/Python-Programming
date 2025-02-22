import re

text = "The price is $19.99 and the discount is 15%"
numbers = re.findall(r'\d+\.\d+|\d+', text)
print("Numbers:",numbers)

