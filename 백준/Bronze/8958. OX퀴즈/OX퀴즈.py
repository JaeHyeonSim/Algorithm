import sys

n = int(sys.stdin.readline())
for i in range(n):
    result = sys.stdin.readline().rstrip('\n')
    result = result.split('X')
    
    total = 0
    for r in result:
        score = len(r)
        total += score * (score + 1) // 2
        
    print(total)