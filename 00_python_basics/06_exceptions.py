"""Exception (ngoại lệ) cơ bản."""

try:
    x = int(input("Nhập số nguyên: "))
    print(10 / x)
except ValueError:
    print("Không phải số nguyên")
except ZeroDivisionError:
    print("Không thể chia cho 0")
