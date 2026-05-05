'''file handling in python in write mode '''

# f = open("file.txt",'w')
# # print(f.tell()) - cursor postion initially
# # f.write("iron man\n")
# l1=["iron man\n", "super man\n", "spider man\n"] - writting  multiple strings
# # f.writelines(l1)
# # print(f.read()) - unsupported operation
# f.close()

# in this if we write anything new means it will override the previous one


'''In read mode '''

# f = open("file.txt", 'r')
# print(f.tell())
# s=f.read() #- reads whole file but if we give like f.read(4) it will ive only characters which i mentioned in the brackets
# print(s)
# f.seek(3)
# print(f.tell())
# f.close()


'''using with keyword means to create a with block inside the block file, to open and close automatically the mode of operation '''

# with open("file.txt",'w') as f:
#  d= f.write("salman khan\n")
#  print(d)


'''append mode '''

# f=open("file.txt",'a')
# f.write("sharukh khan\n")
# f.close()


'''create mode '''

# f= open("file.txt", 'x')
# f.write("iron man\n")  # if file exist it will show file exist error.


'''based on file handling some programs'''

# # step 1 - writing of file.

# with open("student.txt",'w') as f:
#     f.write("student-name : Rahul.\n")
#     f.write("age:22.\n")

# print("file written succesfully.\n") 


# # step 2 - read and display the contents of the file

# print("reading the file:")

# with open("student.txt",'r') as f:
#     data=f.read()
#     print(data)

# print("-----------------------------------")    


# # step 3 - append new content to the file.
# with open("student.txt",'a') as f:
#     f.write("branch:computer science.\n")
#     f.write("course: python fullstack.\n")

# print("new data added succesfully.\n")  

# print("----------------------------------")


# # step 4 Read and display the updated contents of the file
# print("Reading the updataed file.\n")

# with open("student.txt",'r') as f:
#     new_data=f.read()
#     print(new_data)



