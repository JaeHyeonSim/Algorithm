import sys

n = int(input())

nums = list()
for i in range(n):
    nums.append(int(sys.stdin.readline()))

for num in sorted(nums):
    print(num)