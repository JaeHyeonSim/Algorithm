import sys

total = 0
for i in range(4):
    total += int(sys.stdin.readline())

print(total // 60)
print(total % 60)