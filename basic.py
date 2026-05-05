# '''python'''

# ''' 1.what is python '''
# # python is a high level, interpreted, programming and scripting language
# #   which supports both functional and object oriented programming.

# '''features'''
# # easy to learn and easy to understand and very less code and open source and platform independent 
# # and dynamically typed and vast inbuilt methods and vast libraries.


# '''applications'''
# # support for webpage and backend improvement,AI, DS and scientific computing ,system programming, GUI programming 
# # internet scripting , component integration, database programming, rapid prototyping, numeric and scientific programming
# # gaming and image , datamining and robotics.

# '''keywords(35 are their now in python's new version)'''
# # predefined and reserved words by the developer itself are known as keywords.(special keywords - True,False and 
# # None),(soft keywords - '-','case','match','type')

# '''variables'''
# # Name given to a value,that stored in memory location.

# '''Memory Allocation in python'''
# # 1.variable space or stack space.
# # 2.value space or heap spcae.


# '''identifiers'''
# # these are the names which are used to define a set a values or an operation or a class identifiers can be
# # a variable name or it can be a class name or it can be function name.
# # these are either given by user or developers.
# # to create a valid identifier name we have to follow six basic rules.
# # not valid identifier 1.True, 2.1abc, 3.a&c ,4.  ab , 5.should not exceed 31 character according to ISR 

# '''Datatypes'''
# '''1.primitive datatypes'''
# # 1.integer, 2.float, 3.complex, 4.boolean, 5.string

# '''2.Non-primitive'''
# #1.built-in
# # 6.list, 7.tuple, 8.set, 9.dictionary.

# #2.userdefined - 1.linear 2.non-linear
# # array,stack,queue,and linked list are linear
# # graph and tree are the non linear data types

# '''operators - 1.based on operands,2.based on operation,3.special operator'''
# # 1.based on operands
# # 1.unary, 2.Binary, 3.teranary

# # 2.based on operations
# # 1.Arithamatic (+,-,*,/,%,//,**)
# # 2.Relational/comparision (==,<,>,<=,>=,!=)
# # 3.Logical (OR, AND,NOT)
# # 4.Bitwise (&,|,^,<<,>>,~)
# # 5.Assignment (=)- shorthand assignment (+=,-=,*=,/=,%=,**=,//=,&=,|=,^=,<<=,>>=)

# # 3.special operator
# # 1.membership operator - 1.In,2.Not In
# # 2.Identity operator - 1.Is,,2.Is Not
# # 3.slicing - :
# # 4.dot - .
# # 5.Decoration - @

# '''control statements'''
# # the statements which are used control the flow of execution of a program is called as control statements.

# # its divided into two more types
# #1. branching and 2.looping
# # 1.branching - 1.if 2.if else 3.if elif 4.nested if 5.match case 
# # 2.looping - 1.for 2.while , keywords 1.break 2.continue 3.pass

# '''branching or conditionals statements'''

# '''wap for even and odd'''
# # n= int(input("enter a number:"))
# # if n%2==0:
# #     print("even number")
# # else:
# #     print("odd number")

# '''for converting integer to character and character to integer'''
# # print(ord("a"))
# # print(chr(97))


# # print("Uppercase Letters:")
# # for i in range(65, 91):      # A–Z
# #     print(i, "=", chr(i))

# # print("\nLowercase Letters:")
# # for i in range(91, 123):     # a–z
# #     print(i, "=", chr(i))

# # print("\nNumeric Digits:")
# # for i in range(48, 58):      # 0–9
# #     print(i, "=", chr(i))

# # print("\nSpecial Characters:")
# # # Special characters are between 32–47, 58–64, 91–96, 123–126
# # for i in list(range(32, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127)):
# #     print(i, "=", chr(i))

# # Print ASCII values of characters using ord()
# # for ch in (chr(i) for i in range(1, 127)):   # generate characters from ASCII 1–126
# #     print(ch, "=", ord(ch))



# '''wap for to print the entered number is single, two, three digit number or not'''
# # n=int(input("enter a number:"))
# # if n>0 and n<10:
# #     print("entered number is single digit ")
# # elif n>10 and n<100:
# #     print("entered number is two digit")
# # elif n>100 and n<1000:
# #     print("entered number is three digit")
# # else:
# #     print("more than single,two and three digit")

# '''wap for to check the entered character is vowel or not'''
# # char=input("enter a charcater:")
# # vowel=["a","e","i","o","u"]
# # if char in vowel:
# #     print("the entered character is vowel")
# # else:
# #     print("entered charcter is not a vowel")


# '''wap program for entered charcter is vowel or not'''
# # char=input("enter a character:")
# # if (ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=120):
# #     print("entered charcter is alphabet")
# # else:
# #     print("entered charcter is not alphabet")


# '''wap to check the entered number is divisible by 7 or not'''
# # n=int(input("enter a number:"))
# # if n%7==0:
# #     print("the number is divisible by 7")
# # else:
# #     print("entered number is not divisible by 7")

# '''nested if''' #-if the first condition is satisfied then only it go to nested condition otherwise it goes to else 

# '''example'''
# # numbers = [5, 6, 9, 10, 12, 15, 18, 20, 21, 30]

# # for num in numbers:
# #     if num % 2 == 0:
# #         print(num, "is divisible by 2")

# #         if num % 3 == 0:
# #             print(num, "is also divisible by 3")
# #         else:
# #             print(num, "is not divisible by 3")
# #     else:
# #         print(num, "is not divisible by 2")

# #     print()  # for spacing

# '''example'''
# # numbers = [10, 12, 15, 20, 30, 45, 50, 60, 75]

# # for num in numbers:
# #     if num % 2 == 0:
# #         print(num, "is divisible by 2")

# #         if num % 3 == 0:
# #             print(num, "is also divisible by 3")

# #             if num % 5 == 0:
# #                 print(num, "is divisible by 5 too")
# #             else:
# #                 print(num, "is not divisible by 5")
# #         else:
# #             print(num, "is not divisible by 3")
# #     else:
# #         print(num, "is not divisible by 2")

# #     print()  # spacing


# '''match case'''
# # it allows us to perform pattern matching on a variable
# # case numbers can be int,float,string,bool datatypes
# # case _ is wild card xase like else part in conditions

# '''example'''
# # day = input("Enter a day (Mon/Tue/Wed/Thu/Fri/Sat/Sun): ")

# # match day:
# #     case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":
# #         print("It's a weekday")
# #     case "Sat" | "Sun":
# #         print("It's a weekend")
# #     case _:
# #         print("Invalid day")


# '''looping'''
# # these are the statements used repeat the block of code based on the conditions.
# '''for loop - Purpose: Used to iterate over a sequence of items (list, tuple, string, range, etc.) a known number of times.

# Control: Loop runs for each item in the sequence; you generally know how many times it will run.'''
# # 1.using range() 2.using itarable()

# # syntax
# # for variable in range(start,stop,step value):
# # statements

# '''example'''
# # for i in range(1,10,1):
# #     print(i,end=" ")

# # reverse
# # for i in range(10,1,-1):
# #     print(i,end=" ")

# # default start value - 0, step value - 1, stop value  is mandatory or compulsory

# '''example'''
# # for i in range(10):
# #     print(i,end=" ")

# '''using iterable'''
# # names=["rahul","rohit","samarth","kiran"]
# # for name in names:
# #     print(name,end=" ")


# '''nested for loop'''
# # for i in range(1,5):
# #     for j in range(1,4):
# #         for k in range(1,3):
# #           print(k,end=" ")



# '''while loop - it is used to repeat a block of code untill the condition becomes true'''
# # syntax - initialization - start value
# # while condition - stop value
# # updation - step value
# # updation and initialization  are compulsory
# # when stop value is not mentioned the loop will run infinatelly and without updation also it will run infinatelly.

# '''example'''
# # i=0
# # while i<=11:
# #     print(i,end=" ")
# #     i+=1

# '''even nuumbers '''
# # i=1
# # while i<=20:
# #     if i%2==0:
# #         print(i,end=" ")
# #     i+=1    


# '''product of given list'''
# # l1=[1,2,3,4,5]
# # product=1
# # for i in l1:
# #     product*=i
# # print(product)  


# '''keywords'''

# '''break - it is used to forcefully stop the loop or terminate the loop based on the condition'''
# '''example'''
# # for i in range(1,10):
# #     if i==2:
# #         break
# #     print(i)


# '''continue - used for forcefully continue the loop with by escaping the condition applied'''
# # for i in range(1,10):
# #     if i==3:
# #         continue
# #     print(i,end=" ")


# '''pass - whenever empty blocks are required we use pass'''
# '''example'''
# # n=int(input("enter a number:"))
# # for i in range(1,10):
# #     if n==3:
# #         pass
# #     else:
# #         print("shaktiman")

# '''Data structures'''
# '''list - group of values separated by comma and enclosed in square brackets'''
# # syntax - list =[value1, value2,.....valuen]
# # properties of list - 1.homogeneous and heterogeneous
# # 2.supports duplicate elements
# # 3.ordered collection
# # 4.supports indexing
# # 5.supports slicing
# # 6.mutable collection


# '''built in methods of list'''
# # there are 11 built methods in list for modifying ,fetching and extracting  the data in list.
# l1 = [1,2,3,4,5,6,7,8]
# l1.append(9)
# l1.extend([1,2,3])
# l1.pop(-1)
# l1.remove(4)
# l1.sort()
# l1.reverse()
# l1.copy()
# l2=l1.count(1)
# l3=l1.index(5)
# l1.insert(2,3)
# l1.clear()
# print(l1)
# print(l2)
# print(l3)

'''tuple - set of homogeneous and heterogeneous values enclosed within a pair of  paranthesis separated by comma  '''
# t=(1,2,3,4,5,6,7)
# t1=t.count(2)
# t2=t.index(4)
# print(t)
# print(t1)
# print(t2)

'''set - group of values enclosed between a pair of curly brackets and which does not allows duplicates and unorder collection of data '''
# s1={1,2,3,4,5,6,7,7}
# s1.add(8)
# s1.pop()
# s1.remove(3)
# s1.discard(10)
# # s2=s1.copy()
# # s1.update([9,0,10,"rahul"])
# # s2=s1.union({11,12,1,2})
# s2=s1.intersection({22,33})
# print(s1)
# print(s2)

'''dictionary - collection of items means key value pair separated with colon and items areseparated with comma enclosed in a curly brackets'''
# d={"one":1,"two":2,"three":3}
# d.copy()
# d1=d.get("one")
# l1=d.items()
# d3=d.keys()
# d4=d.values()
# t=d.fromkeys("f",4)
# d.update({"one":4})
# d.popitem()
# d.pop("two")
# i=d.setdefault("one",400)
# print(d)
# print(d1)
# print(l1)
# print(d3)
# print(d4)
# print(i)
# print(t)




