n = int(input())
answer = list(input())

for i in range(n - 1):
    f_name = list(input())
    for j in range(len(answer)):
        if f_name[j] != answer[j]:
            answer[j] = '?'

print(''.join(answer))