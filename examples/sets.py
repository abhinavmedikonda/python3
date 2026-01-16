bkt = {1, 2, 3, 'a', 'b', 'c'}
bkt.add(4)
bkt.update([4, 5])
bkt.remove(4)
# tot.remove(4) # error on no match
bkt.discard(4)
[bkt.discard(it) for it in ['a', 'b', 'c']]
lst = sorted(bkt, key = lambda x: x)
print(type(lst), lst)

bkt2 = {3, 4, 5, 6}
print(bkt.isdisjoint(bkt2))
unin = bkt.union(bkt2)
intr = bkt.intersection(bkt2)

