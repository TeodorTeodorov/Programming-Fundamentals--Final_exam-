import re

text = input()

pattern = r'(:{2}|\*{2})([A-Z][a-z]{2,})(\1)'
    # r'[\*\:]{2}[A-Za-z]+[\*\:]{2}' # ---->
matches = re.findall(pattern, text)

pater_num = r'\d'
maches_num = re.findall(pater_num, text)
suma = 1
for index in range(len(maches_num)):
    suma *= int(maches_num[index])

print(f'Cool threshold: {suma}')

print(f"{len(matches)} emojis found in the text. The cool ones are:")
for words in matches:
    ord_sum = 0
    for index in range(len(words[1])):

        ord_sum += ord(words[1][index])
    if ord_sum > suma:
        print(''.join(words))







