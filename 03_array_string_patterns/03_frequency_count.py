"""Frequency counting (đếm tần suất)."""

from collections import Counter

a = [4, 1, 4, 2, 1, 4]
freq = Counter(a)
print(freq)
print(freq.most_common(1))
