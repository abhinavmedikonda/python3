age = int(input("how old are you?\n"))

floating = age / 10
print(floating)
decades = age // 10
years = age % 10

print("you are " + str(decades) + " decades and " + str(years) + " years old")
print(f"you are {decades} decades and {years} years old")

isold = False
isold = age > 50
print(isold)
isold = 23
print(isold)
