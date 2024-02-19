scale = list(map(int, input().split()))

isAscending = True
isDescending = True
for i in range(1, 8):
    if scale[i] < scale[i - 1]:
        isAscending = False
    if scale[i] > scale[i - 1]:
        isDescending = False

if isAscending and (not isDescending):
    print("ascending")
elif isDescending and (not isAscending):
    print("descending")
else:
    print("mixed")
