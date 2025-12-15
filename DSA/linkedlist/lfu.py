from linkedlist import dll

def new_meta():
    head = dll()
    tail = dll()
    head.next = tail
    tail.prev = head
    return {
        'head': head,
        'tail': tail,
        'len': 0
    }

def new_node(_key, _val):
    return dll({
        'key': _key,
        'val': _val,
        'freq': 1
    })

def remv_node(_node):
    global min_freq
    f = _node.data['freq']
    meta = freq_map.get(f)
    if not meta:
        return -1
    _node.prev.next = _node.next
    _node.next.prev = _node.prev
    meta['len'] -= 1
    if meta['len'] == 0:
        freq_map.pop(f)
        if min_freq == f:
            min_freq += 1


def add_node(_node):
    f = _node.data['freq']
    meta = freq_map.get(f)
    if not meta:
        meta = new_meta()
        freq_map[f] = meta
    tail = meta['tail']
    _node.next = tail
    _node.prev = tail.prev
    tail.prev.next = _node
    tail.prev = _node
    meta['len'] += 1

def raise_node(_node, _val=None):
    remv_node(_node)
    _node.data['freq'] += 1
    if _val:
        _node.data['val'] = _val
    add_node(_node)

def get(_key):
    node = key_map.get(_key)
    if not node:
        return -1
    raise_node(node)
    return node.data['val']

def put(_key, _val):
    global min_freq
    node = key_map.get(_key)
    if node:
        raise_node(node, _val)
        return
    if len(key_map) == cap:
        node = freq_map[min_freq]['head'].next
        remv_node(node)
        key_map.pop(node.data['key'])
    node = new_node(_key, _val)
    add_node(node)
    key_map[_key] = node
    min_freq = 1

def delete(_key):
    node = key_map.get(_key)
    if not node:
        return -1
    remv_node(node)
    key_map.pop(_key)

cap = 5
key_map = {}
freq_map = {}
min_freq = 0

if __name__ == '__main__':
    put(1, 'a')
    put(2, 'b')
    put(3, 'c')
    put(4, 'd')
    put(5, 'e')
    print(get(1))  # 'a'
    print(get(2))  # 'b'
    put(6, 'f')    # evicts key 3
    print(get(3))  # -1
    put(2, 'bb')   # update key 2
    print(get(2))  # 'bb'