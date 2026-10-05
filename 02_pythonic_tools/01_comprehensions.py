"""Comprehension: cú pháp tạo collection ngắn gọn."""

squares = [x * x for x in range(10) if x % 2 == 0]
unique_lengths = {len(s) for s in ["a", "bb", "ccc", "dd"]}
lookup = {x: x * x for x in range(5)}
print(squares, unique_lengths, lookup)
