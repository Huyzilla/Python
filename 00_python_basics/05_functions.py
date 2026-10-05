"""Hàm, tham số và giá trị trả về."""

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

print(gcd(24, 18))
