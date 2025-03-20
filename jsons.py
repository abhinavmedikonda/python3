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
for item in json['people']:
    print(item['name'], '-', item['craft'])