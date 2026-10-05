"""Bit manipulation (thao tác bit) cơ bản."""

x = 10  # 1010
print(x & 1)          # kiểm tra bit cuối
print(x | (1 << 0))   # bật bit 0
print(x & ~(1 << 1))  # tắt bit 1
print(x ^ (1 << 2))   # đảo bit 2
print((x >> 1) & 1)   # đọc bit 1
