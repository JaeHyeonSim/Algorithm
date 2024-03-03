n, k = map(int, input().split())

k = min([k, n - k])
numerator = 1
denominator = 1

for i in range(n, n - k, -1):
    numerator *= i
for i in range(k, 0, -1):
    denominator *= i

print(numerator // denominator)