uniq = {1, 2, 3, 'a', 'b', 'c'}
uniq.add(4)
uniq.update([4, 5])
uniq.remove(4)
# tot.remove(4) # error on no match
uniq.discard(4)
[uniq.discard(it) for it in ['a', 'b', 'c']]
lst = sorted(uniq, key = lambda x: x)
print(type(lst), lst)

bckt2 = {3, 4, 5, 6}
print(uniq.isdisjoint(bckt2))
unin = uniq.union(bckt2)
intr = uniq.intersection(bckt2)
uniq.intersection_update(bckt2)
print(uniq)
bckt3 = bckt2 - uniq
print(type(bckt3), bckt3)
