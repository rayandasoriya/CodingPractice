def minMeetingRooms(intervals):
    if intervals is None or len(intervals) == 0:
        return 0
    tmp = []
    for inter in intervals:
        tmp.append((inter[0], True))
        tmp.append((inter[1], False))

    tmp = sorted(tmp, key=lambda v: (v[0], v[1]))
    print(tmp)
    n = 0
    max_num = 0
    for arr in tmp:
        if arr[1]:
            n += 1
        else:
            n -= 1
        max_num = max(n, max_num)
    return max_num


intervals = [[0, 30],[5, 10],[15, 20]]
print(minMeetingRooms(intervals))