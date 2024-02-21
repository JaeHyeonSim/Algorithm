import sys

t = int(sys.stdin.readline())

for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    
    floor = n % h
    room = n // h % w + 1
    if n % h == 0:
        floor = h
        room -= 1
        if n // h == w:
            room = w
        
    print(floor * 100 + room)