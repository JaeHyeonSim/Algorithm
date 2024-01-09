x = int(input())

mini = 64
total = 64
answer = 1

while total > x:
    mini //= 2
    answer += 1
    if total - mini >= x:
        total -= mini
        answer -= 1

print(answer)