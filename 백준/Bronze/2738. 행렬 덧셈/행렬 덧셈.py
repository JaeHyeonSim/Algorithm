n, m = map(int, input().split())
mat1, mat2 = [], []
for i in range(n):
    mat1 += list(map(int, input().split()))
for i in range(n):
    mat2 += list(map(int, input().split()))
for i in range(n * m):
    print(mat1[i] + mat2[i], end=" ")