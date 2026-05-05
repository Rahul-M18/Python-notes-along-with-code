# import json

# person = {
#      "name":"alice",
#      "age":22,
#      "from":"america"
# }
# # converting python dictionary into json string
# json_data = json.dumps(person)
# print("JSON string:",json_data)

# # convert json string -> python dict
# python_data =json.loads(json_data)
# print("python dictionary:",python_data)

# # save json to a file
# with open("person.json","w") as file:
#     json.dump(person,file)

# #read json back from file
# with open("person.json","r") as file:
#     loaded_person =json.load(file)

# print("loaded from file:",loaded_person)  

'''pickle'''
import pickle

# Example object (a Python dictionary)
data = {"name": "Alice", "age": 30, "city": "New York","phone number":9609737865}

# --- Serialize (pickle) the object ---
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# --- Deserialize (unpickle) the object ---
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)

