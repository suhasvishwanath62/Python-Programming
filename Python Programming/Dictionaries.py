person = {
    "name" : "suhas",
    "age" : 21,
    "profession" : "Engineer"
}
print(person)

print("-------------------------------------------------------")

fav_books = {"title":"rich dad & poor dad",
             "author":"someone",
             "year":1985}
print(fav_books["title"])

print("-------------------------------------------------------")

person = {
    "name" : "suhas",
    "age" : 21,
    "profession" : "Engineer"
}
print(person["age"]) # Accessing elements in dictionaries.

print("-------------------------------------------------------")

persons = {
    "name":"suhas",
    "age":21
}
persons["city"] = "Bangalore" # Adding new item to dict.
persons["profession"] = "Engineer"
print(persons)

print("-------------------------------------------------------")

person = {"name": "John", "age": 30, "city": "New York"}
del person["age"] # Using del.
print(person)

print("-------------------------------------------------------")

person_det = {"name": "suhas", "age": 21, "city": "New York"}
print(person_det)
persons_det = person_det.pop("age") # Using pop.
print(persons_det)

print("-------------------------------------------------------")

person = {"name": "John", "age": 30, "city": "New York"}
print(person)
last_item = person.popitem() # Using pop for last item.
print(last_item)

print("-------------------------------------------------------")

person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key) # print only the key items.

print("-------------------------------------------------------")

person = {"name": "John", "age": 30, "city": "New York"}
for value in person.values():
    print(value) # print only the values in items.

print("-------------------------------------------------------")

person = {"name": "John", "age": 30, "city": "New York"}
for key,values in person.items():
    print(f"{key}: {values}") # looping through key-value pairs in dict.

print("-------------------------------------------------------")

authors = {"Paulo Coelho": "The Alchemist",
           "George Orwell": "someone",
           "J.K. Rowling": "Harry Potter"}
for author, book in authors.items():
    print(f"Author: {author}, Book: {book}")

print("-------------------------------------------------------")

person = {"name": "John", "age": 30, "city": "New York"}
copy_items = person.copy() # copy creates a duplicate dict.
print(copy_items)

print("-------------------------------------------------------")

person = {"name": "John", "age": 30, "city": "New York"}
person.clear() # clears all the elements in dict.
print(person)

print("-------------------------------------------------------")

person = {"name": "John", "age": 30}
print(person.get("name")) # get is used to get the value of item
print(person.get("city"))
print(person.get("city","unknown")) # we can specify the name for default value:none as 'unknown'.

print("-------------------------------------------------------")

person = {"name": "John", "age": 30}
person.update({"city":"Bangalore","job":"software engineer"})
print(person) # update is used for updating the other dict items to current dict items.

print("-------------------------------------------------------")

# *args and **kwargs.

def fruits(*args):
    for fruit in args:
        print(fruit)
fruits("apple","mango","banana")

print("-------------------------------------------------------")

def calculate_avg(*score):
    return sum(score)/ len(score)
avg_score = calculate_avg(85, 90, 78, 92)
print(f"Average score: {avg_score}")

print("-------------------------------------------------------")

# using **kwargs.

def create_profile(**details):
    for key,value in details.items():
        print(f"{key}: {value}")
create_profile(Name="suhas",age=21,city="Bangalore",Job="Engineer")

print("-------------------------------------------------------")

def log_activity(user_id, *activity, **metadata):
    print(f"User ID: {user_id}")
    print(f"Activities: {activity}")
    print(f"Metadata: {metadata}")
log_activity(101,"login","work","logout",login_id="10101",computer_address="XYZ101")







