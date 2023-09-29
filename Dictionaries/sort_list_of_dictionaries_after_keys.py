from operator import itemgetter

scores = [
    {"name": "Alice", "score": 12},
    {"name": "Charlie", "score": 7},
    {"name": "Bob", "score": 17},
]

print(scores)

# 1. Method
new_scores1 = sorted(scores, key=itemgetter("score"))
print(new_scores1)

# 2. Method
new_scores2 = sorted(scores, key=lambda d: list(d.items())[1])
print(new_scores2)