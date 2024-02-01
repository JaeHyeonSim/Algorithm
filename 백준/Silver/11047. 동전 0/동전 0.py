import sys

n, k = map(int, sys.stdin.readline().split())
a = []
for i in range(n):
    a_i = int(sys.stdin.readline())
    if (a_i <= k):
        a.append(a_i)

answer = 0
for a_i in a[::-1]:
    if k <= 0:
        break
    cnt = k // a_i
    answer += cnt
    k -= a_i * cnt

print(answer)