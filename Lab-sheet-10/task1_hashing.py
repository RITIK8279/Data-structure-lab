
# Open Hashing using chaining
table = [[] for _ in range(5)]

def insert_open(x):
    table[x % 5].append(x)

for x in [10, 15, 20, 7]:
    insert_open(x)

print("Open Hashing:", table)

# Closed Hashing using linear probing
size = 5
closed = [None] * size

def insert_closed(x):
    global closed, size
    if (sum(v is not None for v in closed) + 1) / size > 0.7:
        old = [v for v in closed if v is not None]
        size = size * 2 + 1
        closed = [None] * size
        for v in old:
            insert_closed(v)
    i = x % size
    while closed[i] is not None:
        i = (i + 1) % size
    closed[i] = x

for x in [10, 15, 20, 7]:
    insert_closed(x)

print("Closed Hashing:", closed)
