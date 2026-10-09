
import time

def linear_search(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1

def binary_search(a, x):
    l, r = 0, len(a)-1
    while l <= r:
        m = (l+r)//2
        if a[m] == x:
            return m
        if a[m] < x:
            l = m+1
        else:
            r = m-1
    return -1

def bubble(a):
    a = a.copy()
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection(a):
    a = a.copy()
    for i in range(len(a)):
        m = min(range(i, len(a)), key=a.__getitem__)
        a[i], a[m] = a[m], a[i]
    return a

def insertion(a):
    a = a.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def quick(a):
    if len(a) <= 1:
        return a
    p = a[len(a)//2]
    return quick([x for x in a if x < p]) + \
           [x for x in a if x == p] + \
           quick([x for x in a if x > p])

def merge(a):
    if len(a) <= 1:
        return a
    m = len(a)//2
    l, r = merge(a[:m]), merge(a[m:])
    out = []
    while l and r:
        out.append((l if l[0] <= r[0] else r).pop(0))
    return out + l + r

def bucket(a):
    if not a or min(a) == max(a):
        return a.copy()
    low, high = min(a), max(a)
    b = [[] for _ in range(10)]
    for x in a:
        i = min(9, int((x-low)/(high-low)*10))
        b[i].append(x)
    return merge([x for group in b for x in group])

data = [40, 10, 30, 5, 20]
for name, fn in [
    ("Bubble Sort", bubble),
    ("Selection Sort", selection),
    ("Insertion Sort", insertion),
    ("Quick Sort", quick),
    ("Merge Sort", merge),
    ("Bucket Sort", bucket)
]:
    start = time.perf_counter()
    result = fn(data.copy())
    elapsed = (time.perf_counter()-start)*1_000_000
    print(name, ":", result, "| Time:", round(elapsed, 2), "us")

sorted_data = sorted(data)
print("Linear Search:", linear_search(data, 30))
print("Binary Search:", binary_search(sorted_data, 30))
