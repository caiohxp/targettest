word = input()
newword = ''
for i in range(len(word)):
    newword = word[i] + newword

print(newword)