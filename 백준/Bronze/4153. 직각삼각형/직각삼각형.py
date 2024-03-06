import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a + b + c == 0:
        break
    
    lengths = [a, b, c]
    lengths.sort()
    if lengths[0] ** 2 + lengths[1] ** 2 == lengths[2] ** 2:
        print("right")
    else:
        print("wrong")