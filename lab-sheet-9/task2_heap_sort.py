
def heap_sort(arr):
    import heapq
    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr))
    return result

data = [40, 10, 30, 5, 20]
print("Original Array:", data)
print("Sorted Array:", heap_sort(data.copy()))
