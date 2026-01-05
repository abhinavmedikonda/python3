def maximumNonOverlappingMeetings(meetings):
    if len(meetings) == 0:
        return 0
    m = sorted(meetings, key = lambda x: x[1])
    _out = 1
    l = m[0][1]
    for it in m[1:]:
        if it[0] >= l:
            _out += 1
            l = it[1]
    return _out


if __name__ == '__main__':
    meetings_rows = int(input().strip())
    meetings_columns = int(input().strip())

    meetings = []

    for _ in range(meetings_rows):
        meetings.append(list(map(int, input().rstrip().split())))

    result = maximumNonOverlappingMeetings(meetings)

    print(result)
