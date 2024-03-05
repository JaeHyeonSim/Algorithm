import sys

n = int(sys.stdin.readline())

members = []
for i in range(n):
    member = sys.stdin.readline().rstrip('\n')
    age = int(member.split()[0])
    members.append([age, i, member])

members.sort(key=lambda x: (x[0], x[1]))
for member in members:
    print(member[2])