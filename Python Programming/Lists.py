my_lists = ["cars","bikes","scooters"]
print(my_lists)

print("--------------------------------------------------------")
# Accessing elements in list
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])

print("--------------------------------------------------------")

fruits = ["apple", "banana", "cherry"]
fruits[0] = "pineapple"
print(fruits)

print("--------------------------------------------------------")

fruits = ["apple", "banana", "cherry"]
fruits.append("apple")# Adding element to last of the list.
print(fruits)

print("--------------------------------------------------------")

fruits = ["apple", "banana", "cherry"]
fruits.insert(0,"straberry") # Inserting the element at specific index in list.
print(fruits)

print("--------------------------------------------------------")

fruits = ["apple", "banana", "cherry"]
print(fruits)
del fruits[0] # Deleting the specfic element in list.
print(fruits)

print("--------------------------------------------------------")

fruits = ["apple", "banana", "cherry"]
print(fruits)
popped_fruits = fruits.pop() # popping the last element in  list
print(fruits)

print("--------------------------------------------------------")

fruits = ["apple", "banana", "cherry"]
print(fruits)
popped_fruits = fruits.pop(1) # popping the 'index 1' element in  list
print(f"I eat",popped_fruits.title())

print("--------------------------------------------------------")

fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.remove("apple") # removing elements by names
print(fruits)

print("--------------------------------------------------------")

fruits = ["apple","banana"]
fruits1 = ["cherry","pineapple"]
fruits.extend(fruits1)
print(fruits)

print("--------------------------------------------------------")

fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

print("--------------------------------------------------------")

fruits = ["apple", "banana", "cherry"]
sliced_list = fruits[0:2]
print(sliced_list)

print("--------------------------------------------------------")

squares = [x**2 for x in range(10)]
print(squares)


