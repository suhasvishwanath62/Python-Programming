
# Inheritance allows one class to inherit the attributes and methods of another class.

class Animal:
    def speak(self):
        print("Animal speakes")

class cat(Animal):
    def meow(self):
        print("Cat meawoos")

cat1 = cat()
cat1.speak()
cat1.meow()

