import sys

num_list = []
num = -1
while num != '0':
    num = sys.stdin.readline()[:-1]
    num_list.append(num)

for num in num_list[:-1]:
    length = len(num)
    is_pal = True
    for i in range(length // 2):
        if num[i] != num[length - i - 1]:
            is_pal = False
            break

    if is_pal:
        print('yes')
    else:
        print('no')