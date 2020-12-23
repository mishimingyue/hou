import json

data = {
    'name': 'myname',
    'age': 100,
}
json_str = json.dumps(data)
print(data)
print(type(json_str))
print(json_str)
