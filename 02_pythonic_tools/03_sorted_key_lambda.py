"""sorted, key và lambda."""

a = [("An", 8), ("Binh", 9), ("Chi", 8)]
print(sorted(a, key=lambda item: (-item[1], item[0])))
