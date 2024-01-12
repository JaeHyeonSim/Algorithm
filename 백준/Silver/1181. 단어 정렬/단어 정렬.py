n = int(input())

words = set()
for i in range(n):
    word = input()
    words.add(word)

sorted_words = sorted(words, key = lambda x:(len(x), x))

for i in range(len(sorted_words)):
    print(sorted_words[i])