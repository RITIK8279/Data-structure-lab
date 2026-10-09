import time

for n in [10000, 50000, 100000]:
    arr = list(range(n))
    target = n - 1

    start = time.perf_counter_ns()

    for i in range(n):
        if arr[i] == target:
            break

    end = time.perf_counter_ns()

    print("Size:", n, "Time:", (end - start) / 1000, "microseconds")