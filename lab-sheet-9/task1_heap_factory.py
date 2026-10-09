
import heapq

data = [40, 10, 30, 5, 20]

min_heap = data.copy()
heapq.heapify(min_heap)

max_heap = [-x for x in data]
heapq.heapify(max_heap)

print("Min Heap:", min_heap)
print("Max Heap:", [-x for x in max_heap])
