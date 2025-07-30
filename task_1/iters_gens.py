#use of for loop

nums = [1,2,3,4,6,7,8]

for i in nums:
    print(i)

#replacing with simples iter and next

iternum = iter(nums)

print(next(iternum))
print(next(iternum))
print(next(iternum))
print(next(iternum))
print("Other Code")
print(next(iternum))
print(next(iternum))
print(next(iternum))
print(next(iternum, 'Finished')) #Add default value in order to avoid error upon iter running out

#custom iters

class fibonacci:
    def __init__(self):
        self.val = 0
        self.prev = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.val <= 5:
            temp = self.val
            self.val += self.prev
            self.prev = temp
            return self.val # infinite sequence if you remove IF ELSE (not possible in for)
        else: 
            raise StopIteration

fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))#custom iters

class fibonacci:
    def __init__(self):
        self.val = 0
        self.prev = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.val <= 5:
            temp = self.val
            self.val += self.prev
            self.prev = temp
            return self.val # infinite sequence if you remove IF ELSE (not possible in for)
        else: 
            raise StopIteration

fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))#custom iters

class fibonacci:
    def __init__(self):
        self.val = 0
        self.prev = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.val <= 5:
            temp = self.val
            self.val += self.prev
            self.prev = temp
            return self.val # infinite sequence if you remove IF ELSE (not possible in for)
        else: 
            raise StopIteration

fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
#print(next(fib)) #raises StopIteration
#for custom iters, you need to make default by yourself as well

#yield is used to pause till next is called, essentially pausing till manually called.

#IMPORTANT

#ITERATORS create current state of the iter and next replaces it with the updated state according to the logic in next func

#GENERATORS create a gen with local context of the function once yield is called and once next is called they reload the function and resume form the place yield was called.