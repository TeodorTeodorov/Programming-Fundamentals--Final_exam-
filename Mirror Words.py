import re

text = input()
regex = r'(@|#)([A-Za-z]{3,})(\1{2,})([A-Za-z]{3,})\1'
matches = re.findall(regex,text)
maches_word = []
counter = 0

for word in matches:

    if word[1] == word[3][::-1]:


        maches_word.append(f'{word[1]} <=> {word[3]}')
    counter += 1


if counter > 0:
    print(f"{counter} word pairs found!")
    if not maches_word:
        print("No mirror words!")

    else:
        print('The mirror words are:')
        print(', '.join(maches_word))
else:
    print("No word pairs found!")
    print("No mirror words!")



