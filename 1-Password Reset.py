first_command = input()
new_text = ""

while True:
    second_command = input()
    if second_command == "Done":
        break
    if "TakeOdd" in second_command:
        new_text = first_command[1::2]
        first_command = new_text
        print(first_command)
    elif "Cut" in second_command:
        command, index, lenght = second_command.split()
        first_command = first_command[:int(index)] + first_command[int(index) + int(lenght):]
        print(first_command)
    elif "Substitute" in second_command:
        substring, substitute1, substitute2 = second_command.split()
        if substitute1 in new_text:
            first_command = first_command.replace(substitute1, substitute2)
            print(first_command)
        else:
            print("Nothing to replace!")
print(f"Your password is: {first_command}")
