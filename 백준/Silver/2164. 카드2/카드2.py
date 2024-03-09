n = int(input())

cards = [i for i in range(1, n + 1)]
i = 0
while True:
    if i + 1 >= len(cards):
        break
    cards.append(cards[i + 1])
    i += 2

print(cards[-1])