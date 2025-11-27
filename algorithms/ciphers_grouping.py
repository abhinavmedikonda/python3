def group_ciphers(ss):
    out = []
    while len(ss) > 1:
        found = False
        arr = []
        for i in range(len(ss)-1, 0, -1):
            if are_ciphers(ss[0], ss[i]):
                arr.append(ss.pop(i))
                found = True
        if found:
            arr.append(ss.pop(0))
            out.append(arr)
        else:
            ss.pop(0)
    return out

def are_ciphers(s1, s2):
    if len(s1) != len(s2):
        return False
    o = distance(s1[0], s2[0])

    for i in range(len(s1)):
        if distance(s1[i], s2[i]) != o:
            return False
    return True

def distance(c1, c2):
    d = ord(c2) - ord(c1)
    if d < 0:
        d += 26
    return d

if __name__ == '__main__':
    ss = ["abc", "zab", "oddzs", "xyz", "affpu", "yzx", "def", "bqqmf", "cab"]
    result = group_ciphers(ss)
    print(result)