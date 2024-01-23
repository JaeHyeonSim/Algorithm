import sys

locs = []

n = int(input())
for i in range(n):
    locs.append(list(map(int, input().split())))

locs = sorted(locs, key=lambda x: (x[0], x[1]))

for loc in locs:
    print(*loc)