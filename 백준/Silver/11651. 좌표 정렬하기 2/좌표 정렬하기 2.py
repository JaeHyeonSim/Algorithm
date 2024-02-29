import sys

n = int(sys.stdin.readline())

coors = []
for i in range(n):
    coors.append(list(map(int, sys.stdin.readline().split())))
coors.sort(key=lambda x: (x[1], x[0]))

for coor in coors:
    print(*coor)