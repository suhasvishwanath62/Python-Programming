fruits = {"apple","banana","cherry"}
print(fruits)
# or
fruits = (["apple","banana","cherry"])
print(fruits)

print("----------------------------------------------------")

fruits = {"apple","banana","cherry"}
print("apple" in fruits)

print("----------------------------------------------------")

fruits = {"apple","banana","cherry"}
print("mango" in fruits)

print("----------------------------------------------------")

movies = {"max","ball","trino","cadel"}
print(movies)
movies.add("siro")
movies.remove("ball")
print(movies)

print("----------------------------------------------------")

set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1 | set2
print(union_set)

print("----------------------------------------------------")

set1 = {1,2,3}
set2 = {3,4,5}
intersection_set = set1 & set2
print(intersection_set)

print("----------------------------------------------------")

set1 = {1,2,3}
set2 = {3,4,5}
difference_set = set1 - set2
print(difference_set)

print("----------------------------------------------------")

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)

print("----------------------------------------------------")

collection1 = {"Book A", "Book B", "Book C"}
collection2 = {"Book C", "Book D", "Book E"}

# Union
all_books = collection1 | collection2
print("All Books:", all_books)

# Intersection
common_books = collection1 & collection2
print("Common Books:", common_books)

# Difference
unique_books = collection1 - collection2
print("Unique to Collection 1:", unique_books)

# Symmetric Difference
exclusive_books = collection1 ^ collection2
print("Exclusive Books:", exclusive_books)

print("----------------------------------------------------")

fruits = {"apple", "banana", "cherry"}
fruits.copy()
print(fruits)

print("----------------------------------------------------")

fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

print("----------------------------------------------------")

fruits = {"apple", "banana", "cherry"}
poped_fruits = fruits.pop() # pops random items in sets.
print(poped_fruits)


