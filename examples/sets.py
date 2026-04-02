bckt = {1, 2, 3, 'a', 'b', 'c'}
bckt.add(4)
bckt.update([4, 5])
bckt.remove(4)
# tot.remove(4) # error on no match
bckt.discard(4)
[bckt.discard(it) for it in ['a', 'b', 'c']]
lst = sorted(bckt, key = lambda x: x)
print(type(lst), lst)

bckt2 = {3, 4, 5, 6}
print(bckt.isdisjoint(bckt2))
unin = bckt.union(bckt2)
intr = bckt.intersection(bckt2)
bckt.intersection_update(bckt2)
print(bckt)
bckt3 = bckt2 - bckt
print(type(bckt3), bckt3)
