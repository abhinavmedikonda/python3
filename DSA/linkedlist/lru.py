from linkedlist import Dll

def get(_key):
    if _key not in hsh:
        return -1
    nod = hsh[_key]
    evict(nod)
    queue(nod)
    hsh[_key] = nod
    return nod.data[1]

def put(_key, _value):
    nod = hsh.get(_key)
    if len(hsh) >= lnt or _key in hsh:
        evict(nod)
    nod = Dll((_key, _value))
    queue(nod)
    hsh[_key] = nod

def evict(_nod):
    global hed, tai
    if not hed:
        return -1
    if hed is tai:
        hsh.pop(_nod.data[0], None)
        hed = None
        tai = None
    elif not _nod or _nod is hed:
        return evict_head()
    elif _nod is tai:
        _nod.prev.next = None
        hsh.pop(_nod.data[0])
        tai = _nod.prev
    else:
        _nod.prev.next = _nod.next
        hsh.pop(_nod.data[0])
        _nod.next.prev = _nod.prev

def evict_head():
    global hed
    if not hed:
        return -1
    hed.next.prev = None
    hsh.pop(hed.data[0])
    hed = hed.next
    return "done"

def queue(_nod):
    global hed, tai
    if not tai:
        hed = _nod
        tai = _nod
    else:
        tai.next = _nod
        _nod.prev = tai
        _nod.next = None
        tai = _nod

def list_cache():
    nod = hed
    while nod:
        print(nod.data)
        nod = nod.next

hsh = dict()
lnt = 5
hed = None
tai = None
if __name__ == '__main__':
    while True:
        print(f'''\n1. add cache\n2. get cache\n3. delete cache\n4. lru\n5. mru\n6. list cache''')
        match input("Enter: ").strip():
            case '1':
                put(*input("key value: ").strip().split())
            case '2':
                print(get(input("key: ").strip()))
            case '3':
                print(evict(hsh.get(input("key: ").strip())))
            case '4':
                print(hed.data if hed else -1)
            case '5':
                print(tai.data if tai else -1)
            case '6':
                list_cache()
