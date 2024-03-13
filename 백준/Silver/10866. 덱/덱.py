import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()
for i in range(n):
    order = sys.stdin.readline().rstrip('\n')
    
    if order.startswith("push_front"):
        queue.appendleft(int(order.split()[1]))
    elif order.startswith("push_back"):
        queue.append(int(order.split()[1]))
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(queue) == 0:
            print(-1)
        elif order == "pop_front":
            print(queue.popleft())
        elif order == "pop_back":
            print(queue.pop())
        elif order == "front":
            print(queue[0])
        elif order == "back":
            print(queue[-1])