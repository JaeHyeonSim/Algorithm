n = int(input())
answers = []
for i in range(n):
    str = input()
    answers.append(str[0] + str[-1])

for i in answers:
    print(i)