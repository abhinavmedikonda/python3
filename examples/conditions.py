import random

weather = random.choice(['sunny', 'rainy', 'cloudy'])
temperature = random.randint(-50, 50)

print(weather, temperature)

if weather == 'rainy' or temperature < 0:
    print('weather is bad, stay home')
elif weather == 'sunny' and temperature > 30:
    print('its sunny and hot, stay home')
elif weather == 'cloudy' and temperature < 10:
    print('its cold outside, stay home')
else:
    print('enjoy weather outside')



print("good" if temperature > 0 else "cold") # inline


match input('Enter choice: '):
    case '1':
        print('option 1')
    case '2':
        print('option 2')