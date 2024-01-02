t = int(input())
answers = []
for i in range(t):
    a, b = map(int, input().split())
    answers.insert(i, a + b)
for i in range(t):
    print("Case #" + str(i + 1) + ": " + str(answers[i]))