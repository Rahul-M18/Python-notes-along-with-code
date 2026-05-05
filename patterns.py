'''patterns'''
# input ,looping, range(), print()
# for i in range(0,11):
#     print(i,end=" ")
#     print("hello")

# n=int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(i):
#        print("*",end=" ")
#     print()    


# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("1",end=" ")
#     print()  

# k=1
# for i in range(1,n+1):
#     for j in range(1,i*2):
#         print("*",end=" ")
#     # k+=2 
#     print()    
# chr=65
# for i in range(0,n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(chr(65),end=" ")          
#     print()    

# rows=int(input("enter number of rows:"))
# for i in range(7):
#     for j in range(5):
#         if j == 0 or i == 0 or i == 3:
#             print(chr(128031), end="")
#         else:
#             print(" ", end="")
#     print()


# for i in range(n-1):
#     for j in range(i,n):
#         print("",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     for l in range(i+1):
#         print("*",end=" ")

    

# for i in range(n):
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()    
# 
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x * x,
        filter(lambda x: x % 2 == 0, numbers))
)

print(result)


        
       
