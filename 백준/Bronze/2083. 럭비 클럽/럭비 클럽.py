import sys

while True:
    name, age, weight = sys.stdin.readline().rstrip('\n').split()
    if name == '#':
        break
    
    group = "Junior"
    if int(age) > 17 or int(weight) >= 80:
        group = "Senior"
    
    print(name, group)