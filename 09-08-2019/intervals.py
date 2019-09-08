def insert(intervals, newInterval):
    result = []
    i = 0
    while i < len(intervals) and newInterval[0] > intervals[i][1]:
        result.append(intervals[i]),
        i += 1
    while i < len(intervals) and newInterval[1] >= intervals[i][0]:
        newInterval = [min(newInterval[0], intervals[i][0]),max(newInterval[1], intervals[i][1])]
        i += 1
    result.append(newInterval)
    result += intervals[i:]
    return result

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,9]
print(insert(intervals, newInterval))