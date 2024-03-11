import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()
for i in range(n):
    order = sys.stdin.readline().rstrip('\n')
    
    if order.startswith("push"):
        queue.append(int(order.split()[1]))
    elif order == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])