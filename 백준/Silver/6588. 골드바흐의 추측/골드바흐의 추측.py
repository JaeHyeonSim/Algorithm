import sys

prime = [1] * 1000000
for i in range(2, 1000000):
    if i * i >= 1000000:
        break
    for j in range(i * i, 1000000, i):
        prime[j] = 0

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    find = 0
    for i in range(3, n - 2, 2):
        if prime[i] == 1 and prime[n - i] == 1:
            print("{0} = {1} + {2}".format(n, i, n - i))
            find = 1
            break
    if find == 0:
        print("Goldbach's conjecture is wrong.")