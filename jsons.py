# alias python=python3.12
# alias pip=pip3.12
# pip install requests
# pip show requests
import sys
print(sys.version)
import requests

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

print('people currently in space:')
for item in json.get('people'):
    print(item['name'], '-', item['craft'])


print()
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_dict = json.loads(json_string)
print(python_dict)
print(type(python_dict))

json_string = json.dumps(python_dict)
print(json_string)
print(type(json_string))