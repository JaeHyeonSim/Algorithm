import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

result_max = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            now = cards[i] + cards[j] + cards[k]
            if now > result_max and now <= m:
                result_max = now

print(result_max)