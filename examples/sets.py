tot = {1, 2, 3, 'a', 'b', 'c'}
tot.add(4)
tot.update([4, 5])
tot.remove(4)
# tot.remove(4) # error on no match
tot.discard(4)
[tot.discard(it) for it in ['a', 'b', 'c']]
lst = sorted(tot, key = lambda x: x)

print(type(lst), lst)
