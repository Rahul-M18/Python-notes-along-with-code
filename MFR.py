'''Map''' # - applies to ecah element in an iterable. and returns a map object(can be converted into list, tuple etc)
# square of each number 
# n=[1,2,3,4,5]
# square = list(map(lambda x:x**2,n))
# print(square)


'''filter''' # - keeps only to elements that satisfy a condition

# for keeping only even numbers
# num=[1,2,3,4,5,6,7,8,9,10]
# even_num =list(filter(lambda x:x%2==0,num))
# print(even_num)



'''reduce''' # - combine all elements into one

# ex: product of all the numbers
# from functools import reduce
# n=[1,2,3,4,5]
# product=reduce(lambda x,y:x*y,n)
# print(product)
 

'''using all them together'''

# from functools import reduce

# n=[1,2,3,4,5,6]
# square=list(map(lambda x:x**2,n))
# print(square)
# even_sqaure=list(filter(lambda x:x%2==0,square))
# print(even_sqaure)
# result=reduce(lambda x,y:x+y,even_sqaure)
# print("final output is : ",result)


