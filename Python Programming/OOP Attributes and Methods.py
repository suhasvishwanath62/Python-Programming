
# Attributes are variables that belong to an object. They are defined within the __init__ method.

# print Methods are functions defined within a class. They operate on the attributes of the class.

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
person1 = person("suhas",21)
print(person1.name)

print("---------------------------------------------------")

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"My Name is {self.name} and i am {self.age} years old.")
person1 = person("suhas v",21)
person1.greet()

print("---------------------------------------------------")

