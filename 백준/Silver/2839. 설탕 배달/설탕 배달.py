n = int(input())
pb = -1
find = False

# 5n + 3m = 18, n > m 을 만족할 때 n + m 구하기
for i in range(n // 5, -1, -1):
    if not find:
        for j in range((n - (5 * i)) // 3, -1, -1):
            if not find and (5 * i) + (3 * j) == n:
                pb = i + j
                find = True

print(pb)