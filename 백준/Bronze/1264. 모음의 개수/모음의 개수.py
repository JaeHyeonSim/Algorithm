import sys

vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    sentence = sys.stdin.readline().rstrip('\n')
    if sentence == '#':
        break
    
    sentence = sentence.lower()
    total = 0
    for char in sentence:
        if char in vowel:
            total += 1
    
    print(total)