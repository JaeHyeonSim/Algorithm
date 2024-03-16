import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    
    total = 0
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            total += i
            divisors.append(i)
    
    if total == n:
        print(str(n) + " = ", end="")
        print(*divisors, sep=" + ")
    else:
        print(str(n) + " is NOT perfect.")
