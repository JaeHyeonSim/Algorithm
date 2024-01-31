import sys

n, m = map(int, sys.stdin.readline().split())
s = []
for i in range(n):
    s.append(sys.stdin.readline().rstrip('\n'))

answer = 0
for i in range(m):
    str = sys.stdin.readline().rstrip('\n')
    if str in s:
        answer += 1

print(answer)