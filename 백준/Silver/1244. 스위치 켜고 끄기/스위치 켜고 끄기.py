import sys

swi_n = int(sys.stdin.readline())
status = list(map(int, sys.stdin.readline().split()))
stu_n = int(sys.stdin.readline())
for stu in range(stu_n):
    gender, num = map(int, sys.stdin.readline().split())

    if gender == 1:
        for i in range(num - 1, swi_n, num):
            if status[i] == 0:
                status[i] = 1
            else:
                status[i] = 0

    if gender == 2:
        for i in range(min(num, swi_n - num + 1)):
            if status[num - 1 - i] != status[num - 1 + i]:
                break
            
            if status[num - 1 - i] == 0:
                status[num - 1 - i] = 1
                status[num - 1 + i] = 1
            else:
                status[num - 1 - i] = 0
                status[num - 1 + i] = 0

for i in range(swi_n):
    print(status[i], end=" ")
    if (i + 1) % 20 == 0:
        print()