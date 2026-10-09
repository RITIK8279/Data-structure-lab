
from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

matrix = [[0]*4 for _ in range(4)]
for u in graph:
    for v in graph[u]:
        matrix[u][v] = 1

print("Adjacency Matrix:")
for row in matrix:
    print(row)

print("Adjacency List:", graph)

def dfs(start):
    seen = set()
    def visit(u):
        if u in seen:
            return
        seen.add(u)
        print(u, end=" ")
        for v in graph[u]:
            visit(v)
    visit(start)

def bfs(start):
    seen = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        print(u, end=" ")
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)

print("DFS:")
dfs(0)
print("\nBFS:")
bfs(0)
