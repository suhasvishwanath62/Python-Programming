i = 1
while i <= 5:
    print(f"The number is: ",i)
    i += 1

print("-------------------------------------------")

days = 10
while days >= 0:
    print(f"{days} days to go!")
    days -= 1

print("-------------------------------------------")

numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers:
    print(i)

print("-------------------------------------------")

names = ["suhas","kishan","Manjulakshmi","vishwanath"]
for i in names:
    print(f"Name: ",i)

print("-------------------------------------------")

for i in range(1,4):
    print(i)

print("-------------------------------------------")

for i in range(1,4):
    for j in range(1,4):
        print(f"i= {i},j= {j}")

print("-------------------------------------------")

beverages = ["coffee", "Tea"]
snacks = ["cookies", "cake"]
for i in beverages:
    for j in snacks:
        print(f" I will eat {i} with {j}")

print("-------------------------------------------")

for i in range(10):
    if i == 5:
        break # first break and print all the traversed elements
    print(i)

print("-------------------------------------------")

books = ["book a", "book b","book c", "book d"]
for i in books:
    if i == "book c":
        print(f"He found {i}") #print specified value and break
        break

print("-------------------------------------------")

for i in range(6):
    if i == 3:
        continue
    print(f"Value is: ",i)

print("-------------------------------------------")

tasks = ["Task 1", "Task 2", "Task 3"]
completed_task = "Task 2"

for task in tasks:
    if task == completed_task:
        continue #except 'Task 2' print all values
    print(f"Praveen needs to do: {task}")

print("-------------------------------------------")

# The pass statement does nothing and is used as a placeholder in situations
# where code is syntactically required but not needed at the moment.

for i in range(5):
    if i == 3:
        pass # I will update later
    else:
        print(i)




