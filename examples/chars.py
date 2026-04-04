import string

for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end='')
print()
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
