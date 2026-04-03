class Sll:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next: "Sll" = next
    def from_iterable(s, ci=None):
        if not s:
            return None
        op = h = Sll()
        cn = None
        for i, v in enumerate(s):
            h.next = Sll(v)
            h = h.next
            if i == ci:
                cn = h
        h.next = cn
        return op.next
    def print(sll):
        while sll:
            print(sll.data, end=' ')
            sll = sll.next
        print()

class Dll:
    def __init__(self, data=None):
        self.data = data
        self.prev: "Dll" = None
        self.next: "Dll" = None
