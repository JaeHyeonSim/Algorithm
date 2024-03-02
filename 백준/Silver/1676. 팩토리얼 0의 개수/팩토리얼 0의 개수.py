n = int(input())

fac = 1
for i in range(2, n + 1):
    fac *= i

answer = 0
for num in str(fac)[::-1]:
    if int(num) != 0:
        break
    answer += 1

print(answer)