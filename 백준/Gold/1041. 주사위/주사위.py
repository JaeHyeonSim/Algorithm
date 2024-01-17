n = int(input())
dice = list(map(int,input().split()))

sum_two = []
sum_three = []
for i in range(6):
    for j in range(i + 1, 6):
        if (i == 0 and j == 5) or (i == 1 and j == 4) or (i == 2 and j == 3):
            continue
        sum_two.append(dice[i] + dice[j])
        for k in range(j + 1, 6):
            if (i == 0 and k == 5) or (i == 1 and k == 4) or (i == 2 and k == 3):
                continue
            if (j == 0 and k == 5) or (j == 1 and k == 4) or (j == 2 and k == 3):
                continue
            sum_three.append(dice[i] + dice[j] + dice[k])

sum_one = sorted(dice)     
sum_two = sorted(sum_two)
sum_three = sorted(sum_three)

visable_all = pow(n, 3) - pow(n - 2, 3) - pow(n - 2, 2)   # 겉면 정육면체 개수
visable_three = 4   # 3면이 보이는 정육면체 개수
visable_two = 4 * (n - 1) + 4 * (n - 2)  # 2면이 보이는 정육면체 개수
visable_one = visable_all - (visable_three + visable_two)

if n == 1:
    answer = sum(sum_one[:-1])
else:
    answer = visable_one * sum_one[0]
    answer += visable_two * sum_two[0]
    answer += visable_three * sum_three[0]

print(answer)
