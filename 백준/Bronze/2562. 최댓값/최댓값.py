import sys

maxi = 0
index = 0
for i in range(1, 10):
    n = int(sys.stdin.readline())
    if n > maxi:
        maxi = n
        index = i

print(maxi)
print(index)