import re

m = re.fullmatch(r'\+(91){1}\d{10}', '+918274827389')
print('indian number' if m else 'not indian number')

m = re.match(r'^[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', 'dexter@hotmail.co')
print('email' if m else 'not email')

m = re.findall(r'#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3}', '#FfFdF8slfjasfa#aef#f9f9f9#')
print('rgb tags:', m)

m = re.search(r'#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3}', '#FfFdF8slfjasfa#aef#f9f9f9#')
print('first tag:', m.group())

if re.fullmatch(r'(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[A-Za-z0-9]{10}', 'B1CDEF2354'):
    print('''Have at least 2 uppercase letters
Have at least 3 digits
Have no repeated characters
Be exactly 10 characters
Contain only letters and digits''')
else:
    print('Invalid')