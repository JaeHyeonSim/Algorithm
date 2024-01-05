scores = []
for i in range(5):
    scores.insert(i, int(input()))
    if scores[i] < 40:
        scores[i] = 40
print(sum(scores) // 5)