import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    if s == "*":
        break
    
    is_unique = True
    for dist in range(1, len(s)):
        pair_list = []
        for i in range(len(s) - dist):
            pair = s[i] + s[i + dist]
            if  pair in pair_list:
                is_unique = False
                break
            pair_list.append(pair)
            
    if is_unique == True:
        print(s + " is surprising.")
    else:
        print(s + " is NOT surprising.")