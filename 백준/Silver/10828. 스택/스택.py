import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    order = sys.stdin.readline().rstrip('\n')
    
    if order.startswith("push"):
        stack.append(int(order.split()[1]))
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])