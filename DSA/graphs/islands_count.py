
import sys
sys.setrecursionlimit(10**6)

def count_islands(links, n):
    l = list()
    aal = set()
    for item in links:
        l.append(set([item[0], item[1]]))
        aal.update([item[0], item[1]])
    recur(l)
    return len(l) + (n-len(aal))
    
    # l = list()
    # for item in links:
    #     l.append(set([item[0], item[1]]))
    #     oll.update([item[0], item[1]])
    # flag = True
    # while(flag and len(l) > 1):
    #     flag = False
    #     for i in range(len(l)-2, -1, -1):
    #         for j in range(len(l)-1, i, -1):
    #             if not l[i].isdisjoint(l[j]):
    #                 l[i] = l[i].union(l[j])
    #                 l.pop(j)
    #                 flag = True
    # return len(l) + (n-len(oll))

def recur(l):
    for i in range(len(l)-2, -1, -1):
        for j in range(len(l)-1, i, -1):
            if not l[i].isdisjoint(l[j]):
                l[i] = l[i].union(l[j])
                l.pop(j)
                return recur(l)

'''
3
2
0 1
1 2
0 2
4
'''
if __name__ == '__main__':
    links_rows = int(input().strip())
    links_columns = int(input().strip())

    links = []

    for _ in range(links_rows):
        links.append(list(map(int, input().rstrip().split())))

    n = int(input().strip())

    result = count_islands(links, n)

    print(result)
