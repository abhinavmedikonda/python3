hsh = {2: 'a', 'b': 5, 4: 3, 'c': 8, 7: 'b'}
hsh.setdefault(9, []).append(10)
hsh.setdefault(9, []).append(11)
hsh[4] = 3
hsh.pop(4)
hsh.pop(4, -1)
# print(hsh[4]) # error on no match
print(hsh.get(4))

[hsh.pop(it) for it in [2, 7, 9]]
lst = sorted(hsh, key = lambda x: (-hsh[x], x))

for k in hsh:
    print(k)

for k, v in hsh.items():
    print(k, v)