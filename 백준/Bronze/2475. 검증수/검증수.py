total = 0
num_list = input().split()
for i in range(5):
    total += pow(int(num_list[i]), 2)
print(total % 10)