"""Two pointers (hai con trỏ): tìm cặp có tổng target trên mảng tăng."""

def has_pair(a: list[int], target: int) -> bool:
    left, right = 0, len(a) - 1
    while left < right:
        total = a[left] + a[right]
        if total == target:
            return True
        if total < target:
            left += 1
        else:
            right -= 1
    return False

print(has_pair([1, 2, 4, 7, 11], 9))
