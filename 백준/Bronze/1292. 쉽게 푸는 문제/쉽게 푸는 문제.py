a, b = map(int, input().split())

n = 1
seq = []
while len(seq) < b:
    for i in range(n):
        seq.append(n)
        if len(seq) == b:
            break
    n += 1

print(sum(seq[a - 1:b + 1]))