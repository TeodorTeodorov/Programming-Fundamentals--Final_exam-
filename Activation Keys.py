activation_key = input()

while True:
    instructions = input()
    if instructions == "Generate":
        break
    if "Contains" in instructions:
        contains, deff = instructions.split(">>>")
        if not deff in activation_key:
            print("Substring not found!")
        else:
            print(f'{activation_key} contains {deff}')

    elif "Flip" in instructions:
        flip, uper_lower, first_index, sec_index = instructions.split(">>>")
        if uper_lower == 'Upper':
            activation_key = activation_key[:int(first_index)] + activation_key[int(first_index):int(sec_index)].upper() + activation_key[int(sec_index):]
            # activation_key[int(first_index):int(sec_index)].upper()
        else:
            # activation_key[int(first_index):int(sec_index)].lower()
            activation_key = activation_key[:int(first_index)] + activation_key[int(first_index):int(sec_index)].lower() + activation_key[int(sec_index):]
        print(activation_key)

    elif "Slice" in instructions:
        slice, start_index, end_index = instructions.split(">>>")

        activation_key = activation_key[:int(start_index)] + activation_key[int(end_index):]
        print(activation_key)

print(f"Your activation key is: {activation_key}")

