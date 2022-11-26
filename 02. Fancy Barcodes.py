import re

numer = int(input())
for i in range(numer):
    sequence = input()
    pattern = r'\#+([A-Z][A-Za-z0-9]{5,})@\#+'
    result = re.findall(pattern, sequence)

    if not result:
        print('Invalid barcode')
    else:
        pattern2 = r'\d'
        result =str(result)
        result_num = re.findall(pattern2, result)
        if not result_num:
            print('Product group: 00')
        else:
            print(f"Product group: {''.join(result_num)}")
