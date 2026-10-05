"""heapq: min-heap (đống cực tiểu) có sẵn."""

import heapq

h = [5, 1, 4, 2]
heapq.heapify(h)
heapq.heappush(h, 0)
while h:
    print(heapq.heappop(h), end=" ")
