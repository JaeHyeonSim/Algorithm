import sys

num = 1
for i in range(3):
    num *= int(sys.stdin.readline())

result = [0] * 10
for n in str(num):
    result[int(n)] += 1

print(*result, sep="\n")