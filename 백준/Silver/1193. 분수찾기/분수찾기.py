n = int(input())

i = 1
begin = 1
for i in range(n + 1):
    begin = int(i * (i + 1) * 0.5)
    if begin >= n:
        break

diff = begin - n
if i % 2 == 0:
    print(i - diff, "/", diff + 1, sep="")
else:
    print(diff + 1, "/", i - diff, sep="")