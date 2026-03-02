hsh = {2: 'a', 'b': 5, 4: 3, 'c': 8, 7: 'b'}
hsh.setdefault(9, []).append(10)
hsh.setdefault(9, []).append(11)
hsh[4] = 3
hsh.pop(4)
hsh.pop(4, -1)
# print(hsh[4]) # error on no match
print(hsh.get(4))

print(all(hsh[k] for k in hsh))
hsh[1] = 0
print(all(hsh[k] for k in hsh))

[hsh.pop(it) for it in [2, 7, 9]]
lst = sorted(hsh, key = lambda x: (-hsh[x], x))

for k in hsh:
    print(k)

for k, v in hsh.items():
    print(k, v)

from collections import defaultdict
d = defaultdict(int)
print(d[5])
d = defaultdict(float)
print(d[5])
d = defaultdict(lambda: -1)
print(d[5])

from collections import Counter
cntr = Counter([1, 3, 4, 3, 1, 5, 6, 2, 3])
print(cntr)