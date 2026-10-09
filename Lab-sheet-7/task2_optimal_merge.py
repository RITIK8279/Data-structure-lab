
import heapq

sizes = list(map(int, input("Enter file sizes: ").split()))
heapq.heapify(sizes)
total = 0

while len(sizes) > 1:
    a = heapq.heappop(sizes)
    b = heapq.heappop(sizes)
    cost = a + b
    total += cost
    print("Merge:", a, "+", b, "=", cost)
    heapq.heappush(sizes, cost)

print("Minimum total merge cost:", total)
