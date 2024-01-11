x, y, w, h = map(int, input().split())
answer = x

if answer > w - x:
    answer = w - x
if answer > y:
    answer = y
if answer > h - y:
    answer = h - y

print(answer)