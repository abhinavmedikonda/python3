def listFreeTime(meetings):
    if len(meetings) == 0:
        return 0
    m = sorted(meetings, key = lambda x: x[0])
    out_ = []
    end = m[0][1]
    for i in range(len(m)-1):
        if end < m[i+1][0]:
            out_.append((end, m[i+1][0]))
        end = max(end, m[i+1][1])
    return out_

if __name__ == '__main__':
    meetings_rows = int(input().strip())
    meetings_columns = int(input().strip())

    meetings = []

    for _ in range(meetings_rows):
        meetings.append(list(map(int, input().rstrip().split())))

    result = listFreeTime(meetings)

    print(result)
