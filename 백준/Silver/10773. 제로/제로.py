import sys

k = int(sys.stdin.readline())

accounting = []
for i in range(k):
    write = int(sys.stdin.readline())
    if write == 0:
        accounting.pop()
    else:
        accounting.append(write)

print(sum(accounting))