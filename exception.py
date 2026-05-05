'''exception handling syntax''' # - run time errors are the exceptions
# try:
    # doubtful code 
# except:
    # handler code 
# else:
    # resultant code 
# finally:
    # executes always

'''simple examples for exception handling on programs '''
''' for a simple example on the printing the division with exceptation'''

# print("start")
# try:
#  a=int(input("enter a number: "))
#  b=int(input("enter a number: "))
#  c=a/b
# except ValueError as e:
#  print("e")
# else:
#  print(c)
# finally:
#  print("end")



'''with using raise keyword'''

# print("start")
# l1=[10,20,30,40]
# try:
#     i=int(input("index:"))
#     if i<-len(l1) or i>len(l1)-1:
#         raise IndexError 
# except:
#     print("some error has occured")
# else:
#     print(l1[i])
# finally:
#     print("end")



'''multiple handler code'''

# print("start")
# try:
#     a=int(input("a: "))
#     b=int(input("b: "))
#     c=a/b
# except ValueError as e:
#     print("value must be integer")
#     print(e)
# except ZeroDivisionError as e:
#     print("denominator must not be zero")
#     print(e)
# except:
#     print("some error occured")
# else:
#     print(c)
# finally:
#     print("end")


'''custom exception or user define exception'''

# defining two user defined exception
# class AgeLesserError(Exception):
#     pass
# class AgeGreaterError(Exception):
#     pass
# print("start")
# try:
#     age=int(input("enter age: "))
#     if age<21:
#         raise AgeLesserError
#     if age>45:
#         raise AgeGreaterError
# except ValueError as e:
#     print(e)
# except AgeLesserError as e:
#     print("age is below 21")
# except AgeGreaterError as e:
#     print("age is above 45")
# except:
#     print("some error occured")
# else:
#     print("age is valid")
# finally:
#     print("end")


'''with returning message in the exception while raising also possible by using __init__ in class '''




'''calculator'''

# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "division by zero gives infinite"

# while True:
#     print("----simple calculator----")
#     print("1.add")
#     print("2.sub")
#     print("3.mul")
#     print("4.div")
#     print("5.exit")

#     choice=input("enter your choice: ")

#     if choice==5:
#         print("thank you exiting...")
#         break

    

    
       

       