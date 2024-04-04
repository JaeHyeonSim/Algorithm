import sys

while True:
    string = sys.stdin.readline().rstrip('\n')
    if string == '.':
        break
    
    balance = True
    stack = []
    for ch in string:
        if ch in ['(', '[',]:
            stack.append(ch)
        elif ch in [')', ']']:
            if len(stack) == 0:
                balance = False
                break
                
            pop_ch = stack.pop()
            if not ((pop_ch == '(' and ch == ')') or (pop_ch == '[' and ch == ']')):
                balance = False
                break
    if len(stack) > 0:
        balance = False
    
    if balance:
        print("yes")
    else:
        print("no")