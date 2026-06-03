for i in range(5):
    for j in range(5):
        print((i, j))
print()
for i in range(5):
    for j in range(i, 5):
        print((i, j))
print()
for i in range(5):
    for j in range(5-i):
        print((j , j+i))
