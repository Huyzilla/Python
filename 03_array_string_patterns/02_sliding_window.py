"""Sliding window (cửa sổ trượt): tổng lớn nhất của k phần tử liên tiếp."""

def max_sum_k(a: list[int], k: int) -> int:
    if k <= 0 or k > len(a):
        raise ValueError("k không hợp lệ")
    window = sum(a[:k])
    best = window
    for right in range(k, len(a)):
        window += a[right] - a[right - k]
        best = max(best, window)
    return best

print(max_sum_k([2, 1, 5, 1, 3, 2], 3))
