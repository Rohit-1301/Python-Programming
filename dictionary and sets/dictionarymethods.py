# marks={
#     "Rohit":100,
#     "Aman":90,
#     "Aditya":80,
#     "Ghanshyam":70,
# }
# print(marks)
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Rohit":99,"Akshay":88})
# print(marks)
# print(marks.get("Rohit"))
# print(marks.get("Rohan")) #it will show none if the key is not present
# # print(marks["Rohan"]) it will show an error if the key is not present

# Creating a dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# 1. Adding a key-value pair
my_dict['email'] = 'alice@example.com'

# 2. Updating a value
my_dict['age'] = 26

# 3. Removing a key-value pair using pop
removed_value = my_dict.pop('city')

# 4. Getting a value with get (returns None if key is not found)
age = my_dict.get('age')

# 5. Checking if a key exists
has_name = 'name' in my_dict

# 6. Iterating through keys and values
for key, value in my_dict.items():
    print(f'{key}: {value}')

# 7. Getting all keys
keys = my_dict.keys()

# 8. Getting all values
values = my_dict.values() 

# 9. Getting all key-value pairs
items = my_dict.items()

# 10. Clearing all items in the dictionary
# my_dict.clear()

print('Removed value:', removed_value)
print('Age:', age)
print('Has name:', has_name)
print('Keys:', keys)
print('Values:', values)
print('Items:', items)
print('Dictionary after clear:', my_dict)

