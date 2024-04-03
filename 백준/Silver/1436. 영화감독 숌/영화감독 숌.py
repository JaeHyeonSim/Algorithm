import sys

n = int(sys.stdin.readline())

i = 0
end_index = 0
while end_index < n:
    i += 1
    if '666' in str(i):
        end_index += 1

print(i)