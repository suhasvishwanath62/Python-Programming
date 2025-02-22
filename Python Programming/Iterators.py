nums =[2,3,4,5,6,7,8,9]
it = iter(nums)
# print(next(it)) # in this way.
#or
# print(it.__next__(),end=" ")
for i in it:
    print(i,end=" ")

print("\n-------------------------------------")

# Own iterator.

class topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
values = topten()
for i in values:
    print(i)







