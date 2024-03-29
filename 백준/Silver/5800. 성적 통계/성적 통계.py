import sys

k = int(sys.stdin.readline())

for i in range(k):
    scores = list(map(int, sys.stdin.readline().split()))
    scores = scores[1:]
    
    scores.sort(reverse=True)
    gap_max = 0
    for j in range(1, len(scores)):
        gap = scores[j - 1] - scores[j]
        if gap > gap_max:
            gap_max = gap
    
    print("Class", i + 1)
    print("Max {0}, Min {1}, Largest gap {2}".format(scores[0], scores[-1], gap_max))