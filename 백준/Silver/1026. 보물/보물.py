import sys

n = sys.stdin.readline()
list_a = sorted(map(int, sys.stdin.readline().split()))
list_b = sorted(map(int, sys.stdin.readline().split()))
list_b.reverse()

s = 0
for a, b in zip(list_a, list_b):
    s += int(a) * int(b)

print(s)