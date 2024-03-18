import sys
from collections import deque

t = int(sys.stdin.readline())
for case in range(t):
    n, m = map(int, sys.stdin.readline().split())
    docs = list(map(int, sys.stdin.readline().split()))
    docs_que = deque(zip(docs, [i for i in range(n)]))
    
    priorities = sorted(docs, reverse=True)
    
    result = 0
    while docs_que:
        popped = docs_que.popleft()
        if popped[0] < priorities[0]:
            docs_que.append(popped) 
        else:
            result += 1
            priorities.remove(popped[0])
            if popped[1] == m:
                print(result)
                break