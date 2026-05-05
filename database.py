import pymysql

con_obj=pymysql.connect(
    user="root",
    password="rahul#45",
    host="localhost"
)

# Create a cursor object
cur_obj= con_obj.cursor()

# Execute the SQL query to show all databases
cur_obj.execute("SHOW DATABASES")

# Fetch and display all databases
print("Databases available on the server:")
for db in cur_obj:
    print(db)


#     name=input("enter the username: ")
#     age=int(input("enter the age: "))
#     address=input("enter the address:")
#     cur_obj.execute("insert into moviesdb.user_info(username,age,address)values(%s,%s,%s);"(name,age,address))
#     connection.commit()
#     print("data is added")
#     try:
#         cur_obj.execute("select * from moviesdb.user_info;")
#         print("the user details:")
#         for data in cur_obj:
#             print(data)
#     except Exception as e:
#         print(e)
# except Exception as e:
#     print(e)