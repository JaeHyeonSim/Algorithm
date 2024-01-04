import math

t = int(input())
answer = []
for i in range(t):
    n, m = map(int, input().split())
    mCn = math.factorial(m) / (math.factorial(n) * math.factorial(m-n))
    answer.insert(i, int(mCn)) # 1~m 중에서 순서 없이 n개 뽑고 나열, mCn
    
for i in range(t):
    print(answer[i])