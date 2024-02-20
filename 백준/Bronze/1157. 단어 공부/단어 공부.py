word = input()
word = word.upper()

al_count = [0] * 26
max_val = 0
isDupl = False
for ch in word:
    al_count[ord(ch) - 65] += 1
    if al_count[ord(ch) - 65] > max_val:
        max_val = al_count[ord(ch) - 65]
        isDupl = False
    elif al_count[ord(ch) - 65] == max_val:
        isDupl = True

if isDupl:
    print("?")
else:
    print(chr(al_count.index(max_val) + 65))