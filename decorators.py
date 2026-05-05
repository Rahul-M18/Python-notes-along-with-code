'''Decorators'''
# def send_message(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return decorator
        

# @send_message(10)
# def greet():
#     print("i am spider man")

# greet()         

'''example'''
# def my_decorator(func):
#     def inner_function():
#         print("i am no-1")
#         func()
#         print("i will save the worls")
#     return inner_function
# @my_decorator
# def greet():
#     print("i am iron man")
# greet()    
