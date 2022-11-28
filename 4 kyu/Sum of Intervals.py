def sum_of_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    last_interval = list(intervals[0])
    answer = last_interval[1] - last_interval[0]
    for i in intervals:
        if i[0] <= last_interval[1]:
            if not i[1] <= last_interval[1]:
                answer += i[1] - last_interval[1]
                last_interval[1] = i[1]
        else:
            answer += i[1] - i[0]
            last_interval[1] = i[1]
    return answer
