class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end   = end
        self.profit = profit


def binarySearch(job, start):
    # Initialize 'lo' and 'hi' for Binary Search
    lo = 0
    hi = start - 1

    # Perform binary Search iteratively
    while (lo <= hi):
        mid = (lo + hi) // 2
        if( job[mid].end <= job[start].start):
            if (job[mid + 1].end <= job[start].start):
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1


# The main function that returns the maximum possible
# profit from given array of jobs
def schedule(job):
    # Sort jobs according to finish time
    job = sorted(job, key=lambda j: j.finish)

    # Create an array to store solutions of subproblems. table[i]
    # stores the profit for jobs till arr[i] (including arr[i])
    n = len(job)
    table = [0 for _ in range(n)]

    table[0] = job[0].profit;

    # Fill entries in table[] using recursive property
    for i in range(1, n):

        # Find profit including the current job
        inclProf = job[i].profit
        l = binarySearch(job, i)
        if (l != -1):
            inclProf += table[l];

        # Store maximum of including and excluding
        table[i] = max(inclProf, table[i - 1])

    return table[n - 1]


# Driver code to test above function
job = [Job(1, 2, 50), Job(3, 5, 20),
       Job(6, 19, 100), Job(2, 100, 200)]
print("Optimal profit is")
print(schedule(job))
