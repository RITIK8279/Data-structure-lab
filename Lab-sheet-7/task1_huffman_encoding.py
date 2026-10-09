
import heapq

chars = input("Enter characters: ").split()
freq = list(map(int, input("Enter frequencies: ").split()))

heap = []
for i, (ch, f) in enumerate(zip(chars, freq)):
    heapq.heappush(heap, (f, i, ch))

if len(heap) == 0 or len(chars) != len(freq):
    print("Invalid input")
else:
    count = len(heap)

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, count, (left, right)))
        count += 1

    def codes(node, code=""):
        if isinstance(node, str):
            print(node, ":", code or "0")
        else:
            codes(node[0], code + "0")
            codes(node[1], code + "1")

    print("Huffman Codes:")
    codes(heap[0][2])
