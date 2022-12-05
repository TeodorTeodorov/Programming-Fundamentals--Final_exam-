import math
import re

text = input()
pattern = r'(\#|\|)([a-z A-Z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

maches = re.findall(pattern, text)

suma = 0

for index in range(len(maches)):

    suma += int(maches[index][3])

days = math.floor(suma / 2000)

print(f"You have food to last you for: {days} days!")
for index in range(len(maches)):
    print(f"Item: {maches[index][1]}, Best before: {maches[index][2]}, Nutrition: {maches[index][3]}")