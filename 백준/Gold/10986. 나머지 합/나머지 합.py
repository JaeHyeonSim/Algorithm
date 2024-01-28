n, m = map(int, input().split())
seq_a = list(map(int, input().split()))

sum_a = seq_a
remains = [0] * m
for i in range(n):
    if i > 0:
        sum_a[i] += sum_a[i - 1]
    remains[sum_a[i] % m] += 1

answer = 0
for i in range(m):
    cnt = remains[i]
    answer += cnt * (cnt - 1) // 2
answer += remains[0]

print(answer)