n = int(input())

answer = 0
for i in range(n - 1, 0, -1):
    digit_sum = sum([int(j) for j in str(i)])
    if i + digit_sum == n:
        answer = i

print(answer)