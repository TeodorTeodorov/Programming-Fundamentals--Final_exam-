stops = input()

while True:
    command = input()
    if command == 'Travel':
        break
    command = command.split(':')
    if command[0] == 'Add Stop':

        if int(command[1]) in range(len(stops)):
            add, index, string = command[0], command[1], command[2]

            stops = stops[:int(index)]+string+stops[int(index):]
            print(stops)
        else:
            print(stops)
    elif command[0] == 'Remove Stop':
        remove, start_index, end_index = command[0], command[1], command[2]
        start_index = int(start_index)
        end_index = int(end_index)
        if start_index and end_index+1 in range(len(stops)+1):
            replace_index = stops[start_index:end_index+1]
            stops = stops.replace(replace_index, '')
            print(stops)
        else:
            print(stops)
    elif command[0] == 'Switch':
        switch, old_string, new_string = command[0], command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
            print(stops)
        else:
            print(stops)
print(f"Ready for world tour! Planned stops: {stops}")