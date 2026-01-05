def merge_intervals(intervals):
    si = sorted(intervals, key=lambda x: x[0])
    recur_merge(si, 0)
    return si
    
def recur_merge(si, ind):
    if ind >= len(si)-1:
        return
    if si[ind+1][0] <= si[ind][1]:
        si[ind][1] = max(si[ind][1], si[ind+1][1])
        si.pop(ind+1)
        recur_merge(si, ind)
    else:
        recur_merge(si, ind+1)

'''
4
2
1 3
2 6
8 10
15 18
'''
if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = merge_intervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
