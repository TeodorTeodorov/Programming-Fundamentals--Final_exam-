number = int(input())
plants = {}

for num in range(number):
    plant, rarity = input().split('<->')

    if plant not in plants:
        plants[plant] = []
        plants[plant].append(rarity)
    else:
        plants[plant].remove(plants[plant][0])
        plants[plant].append(rarity)

while True:
    command = input()
    if command == "Exhibition":
        break
    command = command.split(': ')
    if command[0] == 'Rate':
        plant, rating = command[1].split(' - ')
        rating = float(rating)
        if plant in plants:

            plants[plant].append(rating)
        else:
            print("error")
    elif command[0] == 'Update':
        plant, new_rarity = command[1].split(' - ')
        if plant in plants:
            plants[plant][0] = new_rarity

        else:
            print("error")

    elif command[0] == 'Reset':
        plant = command[1]
        if plant in plants:

            plants[plant][1] = 0
        else:
            print("error")


print("Plants for the exhibition:")
for plant in plants:
    suma = sum(plants[plant][1:20])/len(plants[plant][1:20])
    print(f'- {plant}; Rarity: {plants[plant][0]}; Rating: {suma:.2f}')
