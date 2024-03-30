word = input()

result = word[0] + word[1] + word[2:][::-1]
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        div1 = word[:i][::-1]
        div2 = word[i:j][::-1]
        div3 = word[j:][::-1]
        
        new_word = div1 + div2 + div3
        
        if new_word < result:
            result = new_word

print(result)