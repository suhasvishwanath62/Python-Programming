class Animal:
    def speak(self):
        print("Animal speeks")

class Dog(Animal):
    def speak(self):
        print("Dog Barks")

class Cat(Animal):
    def speak(self):
        print("cat meow")

animals = [Dog(),Cat()]
for animal in animals:
    animal.speak()
