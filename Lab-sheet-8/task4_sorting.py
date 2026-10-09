
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def bucket_sort(a):
    if not a:
        return a
    low, high = min(a), max(a)
    if low == high:
        return a
    buckets = [[] for _ in range(10)]
    for x in a:
        index = min(9, int((x - low) / (high - low) * 10))
        buckets[index].append(x)
    result = []
    for b in buckets:
        result.extend(insertion_sort(b))
    return result

data = [29, 11, 25, 3, 18, 7]
print("Insertion Sort:", insertion_sort(data.copy()))
print("Bucket Sort:", bucket_sort(data.copy()))
