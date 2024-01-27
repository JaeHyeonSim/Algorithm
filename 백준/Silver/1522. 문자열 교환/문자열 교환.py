s = input()

len_a = s.count('a')
len_s = len(s)
s += s[:len_a]

b_min = s.count('b')
for i in range(len_s):
    len_b = s[i:i + len_a].count('b')
    if b_min > len_b:
        b_min = len_b
    
print(b_min)