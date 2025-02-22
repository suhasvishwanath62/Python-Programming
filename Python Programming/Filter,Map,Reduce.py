from past.builtins import reduce # built-in function used in reduce.

def even(n):
    return n%2==0
nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(even,nums)) # you can use 'list, tuples or sets' to print numbers.
print(evens)

print("-----------------------------------------------")

nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda n : n % 2 != 0,nums))
doubles = list(map(lambda n : n * 2,nums))
sum = reduce(lambda a,b:a+b,doubles)
print(evens)
print(doubles)
print(sum)



