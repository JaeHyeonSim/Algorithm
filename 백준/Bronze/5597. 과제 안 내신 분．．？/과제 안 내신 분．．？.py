import sys

submit_list = [False] * 30
for i in range(28):
    submit = int(sys.stdin.readline())
    submit_list[submit - 1] = True
    
for i in range(len(submit_list)):
    if not submit_list[i]:
        print(i + 1)