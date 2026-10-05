"""itertools: công cụ duyệt tổ hợp."""

from itertools import combinations, permutations, accumulate

a = [1, 2, 3]
print(list(combinations(a, 2)))
print(list(permutations(a, 2)))
print(list(accumulate(a)))
