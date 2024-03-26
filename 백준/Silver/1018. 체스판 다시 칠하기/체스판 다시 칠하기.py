import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    board.append(sys.stdin.readline().rstrip('\n'))

result_min = 64
for row in range(n - 7):
    for col in range(m - 7):
        start = board[row][col]
        re_black = 0
        re_white = 0
        for i in range(8):
            for j in range(8):
                if i % 2 + j % 2 == 1:
                    if board[row + i][col + j] == 'W':
                        re_black += 1
                    if board[row + i][col + j] == 'B':
                        re_white += 1
                else:
                    if board[row + i][col + j] == 'B':
                        re_black += 1
                    if board[row + i][col + j] == 'W':
                        re_white += 1
                    
        result = min(re_black, re_white)
        if  result < result_min:
            result_min = result
    
print(result_min)