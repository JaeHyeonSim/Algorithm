import sys

t = int(sys.stdin.readline())

for i in range(t):
    ps = sys.stdin.readline().rstrip('\n')
    
    stack = []
    result = 'YES'
    for ch in ps:
        if ch == '(':
            stack.append(ch)
        if ch == ')':
            if len(stack) == 0:
                result = 'NO'
                break
            stack.pop()
    if len(stack) > 0:
        result = 'NO'
    
    print(result)