"""Mutability (tính thay đổi được) và copy."""

a = [[1, 2], [3, 4]]
b = a.copy()       # shallow copy - sao chép nông
b[0][0] = 99
print(a)            # phần tử lồng nhau vẫn dùng chung

import copy
c = copy.deepcopy(a)
c[0][0] = -1
print(a, c)
