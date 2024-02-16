n, x = map(int, input().split())
seq_a = list(map(int, input().split()))

for i in seq_a:
    if i < x:
        print(i, end=" ")