word = input('단어 입력: ')

is_pp = True
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        is_pp= False
        break

print(is_pp)