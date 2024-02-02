expression = input().split('-')

plus = sum(list(map(int, expression[0].split('+'))))
minus = 0

for splited_minus in expression[1:]:
    minus += sum(list(map(int, splited_minus.split('+'))))

print(plus - minus)