scores = []
for i in range(8):
    scores.append([i + 1, int(input())])

scores.sort(key=lambda x: x[1], reverse=True)

print(sum([i[1] for i in scores[:5]]))
print(*sorted([i[0] for i in scores[:5]]))