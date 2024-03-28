import sys

n = int(sys.stdin.readline())

cases = []
for i in range(n):
    cases.append(list(map(int, sys.stdin.readline().split()))) 
    cases[i].append(i)
cases.sort(key=lambda x:(x[0], x[1]), reverse=True)

result = [0] * n
for i in range(n):
    rank = 1
    for j in range(i):
        if cases[i][0] < cases[j][0] and cases[i][1] < cases[j][1]:
            rank += 1
    result[cases[i][2]] = rank

print(*result)