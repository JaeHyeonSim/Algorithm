word = input()

result = []
for i in range(len(word)):
    if ord(word[i]) >= 97:
        result.append(chr(ord(word[i]) - 32))
    else:
        result.append(chr(ord(word[i]) + 32))

print(''.join(result))