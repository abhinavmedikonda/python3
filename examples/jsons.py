# alias python=python3.12
# alias pip=pip3.12
# pip install requests
# pip show requests
import sys, requests, json
print(sys.version)

response = requests.get('http://api.open-notify.org/astros.json')
people = response.json().get('people')

print('people currently in space:')
for item in people:
    print(item['name'], '-', item['craft'])

print()

json_string = '{"name": "John", "age": 30, "city": "New York"}'
json_string = "{\"name\": \"John\", \"age\": 30, \"city\": \"New York\"}"
python_dict = json.loads(json_string)
print(python_dict)
print(type(python_dict))

json_string = json.dumps(python_dict)
print(json_string)
print(type(json_string))

print(bytearray(json_string, 'utf-8'))