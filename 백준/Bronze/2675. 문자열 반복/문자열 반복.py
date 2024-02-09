import sys

p = int(sys.stdin.readline())
for i in range(p):
    r, s = map(str, sys.stdin.readline().split())
    repeat_list = [ch * int(r) for ch in s]
    print(''.join(repeat_list))