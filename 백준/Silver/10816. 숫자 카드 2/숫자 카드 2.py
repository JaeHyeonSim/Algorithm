import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cases = list(map(int, sys.stdin.readline().split()))

card_dic = {}
for card in cards:
    if card in card_dic:
        card_dic[card] += 1
    else:
        card_dic[card] = 1

result = []
for case in cases:
    if case in card_dic:
        result.append(card_dic[case])
    else:
        result.append(0)

print(' '.join(map(str, result)))