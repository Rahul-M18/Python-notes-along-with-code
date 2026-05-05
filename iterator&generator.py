'''Iterators'''

# class MyIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current>=self.end:
#             raise StopIteration
#         else:
#             self.current+=1
#             return self.current-1

# my_iter =MyIterator(1,10)

# for value in my_iter:
#     print(value)    


'''generators'''
def mygenerators(start, end):
    while start < end:
        yield start
        start +=1

gen = mygenerators(1,6)
print(next(gen))
print(next(gen))
print(next(gen))
       