heroes_num = int(input())
heroes = {}
for i in range(heroes_num):
    hero_name, hp, mp = input().split()

    heroes[hero_name] = []
    heroes[hero_name] += int(hp), int(mp)

while True:
    command = input()
    if command == 'End':
        break
    deff = 0
    command = command.split(' - ')
    if command[0] == 'CastSpell':
       hero_name, needed_mp, spell_name = command[1], command[2],command[3]
       needed_mp = int(needed_mp)
       if heroes[hero_name][1] > needed_mp:
           heroes[hero_name][1] -= needed_mp
           print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
       else:
           print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1],command[2],command[3]
        heroes[hero_name][0] -= int(damage)
        if heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif command[0] == 'Recharge':
        hero_name, amount = command[1],command[2]
        heroes[hero_name][1] += int(amount)

        if heroes[hero_name][1] > 200:

            deff = heroes[hero_name][1] - 200
            total = int(amount) - deff
            heroes[hero_name][1] = 200
            print(f"{hero_name} recharged for {total} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")
    elif command[0] == 'Heal':
        hero_name, amount = command[1], command[2]
        heroes[hero_name][0] += int(amount)

        if heroes[hero_name][0] > 100:

            deff = heroes[hero_name][0] - 100
            total = int(amount) - deff
            heroes[hero_name][0] = 100

            print(f"{hero_name} healed for {total} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")

for hero in heroes:
    print(f'{hero}\n  HP: {heroes[hero][0]}\n  MP: {heroes[hero][1]}')