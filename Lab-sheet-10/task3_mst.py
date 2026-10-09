
edges = [
    (1, 2, 1),
    (2, 3, 2),
    (1, 3, 3),
    (3, 4, 4),
    (2, 4, 5)
]

# Kruskal's Algorithm
parent = list(range(5))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

mst = []
for u, v, w in sorted(edges, key=lambda e: e[2]):
    a, b = find(u), find(v)
    if a != b:
        parent[a] = b
        mst.append((u, v, w))

print("Kruskal MST:", mst)
print("Kruskal Cost:", sum(w for u, v, w in mst))

# Prim's Algorithm
import heapq

graph = {i: [] for i in range(1, 5)}
for u, v, w in edges:
    graph[u].append((w, v))
    graph[v].append((w, u))

visited = {1}
heap = [(w, 1, v) for w, v in graph[1]]
heapq.heapify(heap)
prim = []

while heap and len(visited) < 4:
    w, u, v = heapq.heappop(heap)
    if v in visited:
        continue
    visited.add(v)
    prim.append((u, v, w))
    for cost, nxt in graph[v]:
        if nxt not in visited:
            heapq.heappush(heap, (cost, v, nxt))

print("Prim MST:", prim)
print("Prim Cost:", sum(w for u, v, w in prim))
