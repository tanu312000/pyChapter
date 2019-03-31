
    def merge_overlapping(self, intervals):
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)
        if (n <= 0):
            return
        stack = []
        stack.append(intervals[0])
        for i in range(1, n):
            top = stack[-1]
            if (top.end < intervals[i].start):
                stack.append(intervals[i])
            elif (top.end < intervals[i].end):
                top.end = intervals[i].end
                stack.pop()
                stack.append(top)
        return stack


    def insert(self, intervals, new_interval):
        n = len(intervals)
        i = 0
        arr_newintervals = (n + 1) * [0]
        while (i < n):
            if (new_interval.start < intervals[i].start):
                arr_newintervals.append(new_interval)
            else:
                arr_newintervals.append(intervals[i])
                i = i + 1
        # intervals.sort(key=lambda x: x.start)
        if (n <= 0):
            return
        stack = []
        stack.append(intervals[0])
        for i in range(1, n):
            top = stack[-1]
            if (top.end < intervals[i].start):
                stack.append(intervals[i])
            elif (top.end < intervals[i].end):
                top.end = intervals[i].end
                stack.pop()
                stack.append(top)
        return stack