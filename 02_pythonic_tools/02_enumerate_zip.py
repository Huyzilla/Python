"""enumerate và zip."""

names = ["An", "Binh", "Chi"]
scores = [8, 9, 7]
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(i, name, score)
