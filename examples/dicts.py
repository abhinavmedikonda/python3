hmap = {2: 'a', 'b': 5, 4: 3, 'c': 8, 7: 'b'}
print(next(iter(hmap, None))) # first or None
hmap.setdefault(9, []).append(10)
hmap.setdefault(9, []).append(11)
hmap[4] = 3
hmap.pop(4)
hmap.pop(4, -1)
# print(hsh[4]) # error on no match
print(hmap.get(4))

print(all(hmap[k] for k in hmap))
hmap[1] = 0
print(all(hmap[k] for k in hmap))

[hmap.pop(it) for it in [2, 7, 9]]
lst = sorted(hmap, key = lambda x: (-hmap[x], x))

for k in hmap:
    print(k)

for k, v in hmap.items():
    print(k, v)

from collections import defaultdict
d = defaultdict(int)
print(d[5])
d = defaultdict(list)
print(d[5])
d = defaultdict(lambda: [1, 2, 3]) # non default type
print(d[5])

from collections import Counter
cntr = Counter([1, 3, 4, 3, 1, 5, 6, 2, 3])
print(cntr)