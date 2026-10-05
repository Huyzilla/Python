"""dict: ánh xạ key -> value."""

freq = {}
for x in [1, 2, 1, 3, 2, 1]:
    freq[x] = freq.get(x, 0) + 1
print(freq)
