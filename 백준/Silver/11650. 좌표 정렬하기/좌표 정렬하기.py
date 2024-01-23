import sys

locs = []

n = int(input())
for i in range(n):
    locs.append(list(map(int, sys.stdin.readline().split())))

locs = sorted(locs)

for loc in locs:
    print(*loc)