import time

for n in [100, 500, 1000]:
    count = 0

    start = time.perf_counter_ns()

    for i in range(n):
        for j in range(n):
            count += 1

    end = time.perf_counter_ns()

    print("Size:", n)
    print("Operations:", count)
    print("Time:", (end - start) / 1000, "microseconds")