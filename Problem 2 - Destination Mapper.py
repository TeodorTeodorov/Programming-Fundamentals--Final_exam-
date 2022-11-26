import re

string = input()
pattern = r'(=|\/)([A-Z][A-Za-z]{3,})\1'
result = re.findall(pattern, string)

suma = 0
dest = []
for destination in result:
    dest.append(destination[1])
    suma += len(destination[1])

print(f"Destinations: {', '.join(dest)}")
print(f"Travel Points: {suma}")