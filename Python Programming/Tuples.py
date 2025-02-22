my_tuple = ("cars","bikes","motorcycles","ship","plain")
print(my_tuple)

print("-----------------------------------------------------")

my_tuple = ("cars","bikes","motorcycles","ship","plain")
print(my_tuple[1])

print("-----------------------------------------------------")

coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)

print("-----------------------------------------------------")

my_tuple = (1,3,5,3,6,3,6,4,4)
print(my_tuple.count(4)) # Counts the How many number of '4' are there in tuples.
print(my_tuple.index(6)) # finds the index of the '6' in tuple it will find only the first '6' index.

print("-----------------------------------------------------")

# nested Tuples
daily_schedule = (("Morning", "Breakfast"), ("Afternoon", "Work"), ("Evening", "Relax"))
for period, activity in daily_schedule:
    print(f"During the {period}, suhas will {activity}.")

print("-----------------------------------------------------")

schedule = (("meetings"),("coding"),("Logout"))
for a in schedule:
    print(f"Daily i need to do {a}")

print("-----------------------------------------------------")

# Unpacking tuple elements.
person = ("John", 25, "Engineer")
name, age, profession = person
print(name)
print(age)
print(profession)

