# https://www.instagram.com/p/DSuKpvfCkxl/

import json

data = {'name': 'Adam', 'age': 21, 'city': 'Delhi'}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

string = '{"name": "Adam", "age": 21, "city": "Delhi"}'
json_data = json.loads(string)
print(json_data)
print(type(json_data))
