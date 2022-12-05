import re

number = int(input())
for i in range(number):

    text = input()
    pattern = r'(.+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^><]{3})<\1'
    result = re.findall(pattern, text)
    if not result:
        print("Try another password!")
    else:
        for words in result:
            maches_list = []
            maches_list.append(words[1:])

            for i in maches_list:
                print(f"Password: {''.join(i)}")

# for password in maches_list:
#     if not password:
#         print("Try another password!")
#     else:
#         print(f"Password: {''.join(password)}")
#
