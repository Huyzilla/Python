"""bisect: binary search (tìm kiếm nhị phân) trên list đã sắp xếp."""

from bisect import bisect_left, bisect_right, insort

a = [1, 2, 2, 4, 7]
print(bisect_left(a, 2), bisect_right(a, 2))
insort(a, 3)
print(a)
