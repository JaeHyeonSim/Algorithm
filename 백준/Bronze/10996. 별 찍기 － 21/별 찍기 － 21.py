n = int(input())

for i in range(n):
    for top in range(n):
        if top % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    
    for bottom in range(n):
        if bottom % 2 != 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()