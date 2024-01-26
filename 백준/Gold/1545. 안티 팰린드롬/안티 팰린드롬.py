chars = list(input())

chars.sort()
is_pal = False
mid = len(chars) // 2 + len(chars) % 2
for i in range(mid, len(chars)):
    if chars[i] != chars[len(chars) - 1 - i]:
        continue
    
    is_pal = True
    for j in range(i, len(chars)):
        if chars[i] != chars[j]:
            chars[i] = chars[j]
            chars[j] = chars[len(chars) - 1 - i]
            is_pal = False
            break
    if is_pal:
        break

if is_pal:
    print(-1)
else:
    print(''.join(chars))