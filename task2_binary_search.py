import time

for n in [10000, 50000, 100000]:
    arr = list(range(n))
    target = n - 1

    start = time.perf_counter_ns()

    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    end = time.perf_counter_ns()

    print("Size:", n, "Time:", (end - start) / 1000, "microseconds")