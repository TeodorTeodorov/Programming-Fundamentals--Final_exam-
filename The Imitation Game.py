encrypted_message = input()

while True:
    command = input()
    if command == 'Decode':
        break

    if "Move" in command:
        operation, num_of_letters = command.split('|')
        for i in range(len(encrypted_message)-1):
            if i == int(num_of_letters):
                break
            encrypted_message += encrypted_message[0]
            encrypted_message = encrypted_message.replace(encrypted_message[0], '',1)



    elif "Insert" in command:
        operation, index, value = command.split('|')
        encrypted_message = encrypted_message[:(int(index))]+value+encrypted_message[(int(index)):]


    elif "ChangeAll" in command:
        operation, substring, replacement = command.split('|')
        for i in range(len(encrypted_message)):
            if encrypted_message[i] == substring:
                encrypted_message = encrypted_message.replace(encrypted_message[i], replacement)
print(f"The decrypted message is: {encrypted_message}")
