# pip install requests
# pip show requests
import requests

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

print('people currently in space:')
for item in json['people']:
    print(item['name'], '-', item['craft'])