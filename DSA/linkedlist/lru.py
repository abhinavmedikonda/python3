from linkedlist import dll

def get_cache(key):
    if key not in hsh:
        return -1
    nod = hsh[key]
    evict(nod)
    queue(nod)
    hsh[key] = nod
    return nod.data[1]

def add_cache(key, value):
    nod = hsh.get(key)
    if len(hsh) >= lnt or key in hsh:
        evict(nod)
    nod = dll((key, value))
    queue(nod)
    hsh[key] = nod

def evict(nod):
    global hed, tai
    if not hed:
        return -1
    if hed is tai:
        hsh.pop(nod.data[0], None)
        hed = None
        tai = None
    elif not nod or nod is hed:
        return evict_head()
    elif nod is tai:
        nod.previous.next = None
        hsh.pop(nod.data[0])
        tai = nod.previous
    else:
        nod.previous.next = nod.next
        hsh.pop(nod.data[0])
        nod.next.previous = nod.previous

def evict_head():
    global hed
    if not hed:
        return -1
    hed.next.previous = None
    hsh.pop(hed.data[0])
    hed = hed.next

def queue(nod):
    global hed, tai
    if not tai:
        hed = nod
        tai = nod
    else:
        tai.next = nod
        nod.previous = tai
        nod.next = None
        tai = nod

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
                add_cache(*input("key value: ").strip().split())
            case '2':
                print(get_cache(input("key: ").strip()))
            case '3':
                print(evict(hsh.get(input("key: ").strip())))
            case '4':
                print(hed.data if hed else -1)
            case '5':
                print(tai.data if tai else -1)
            case '6':
                list_cache()
