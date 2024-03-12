n, k = map(int, input().split())

circle = [i for i in range(1, n + 1)]
result = []
r_index = 0

for i in range(n):
    r_index += k - 1
    r_index %= len(circle)
    
    result.append(circle[r_index])
    del circle[r_index]

print('<', end='')
print(*result, sep=', ', end='')
print('>')
