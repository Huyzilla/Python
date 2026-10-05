"""Một số cấu trúc hữu ích trong collections."""

from collections import Counter, defaultdict, deque

print(Counter("abracadabra").most_common(3))
graph = defaultdict(list)
graph[1].append(2)
q = deque([1, 2, 3])
q.appendleft(0)
print(graph, q)
