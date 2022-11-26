number_of_cars = int(input())
cars = {}
for i in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    if car not in cars.keys():
        cars[car] = []
        cars[car].append(int(mileage))
        cars[car].append(int(fuel))



while True:
    command = input()
    if command == 'Stop':
        break

    if 'Drive' in command:
        command1, car_type, distance, needed_fuel = command.split(' : ')
        if car_type in cars.keys():


            # if current_car == cars[current_car]:
            if cars[car_type][1] > int(needed_fuel):
                cars[car_type][1] -= int(needed_fuel)
                cars[car_type][0] += int(distance)
                print(f"{car_type} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
            else:
                print("Not enough fuel to make that ride")
            if cars[car_type][0] >= 100000:
                print(f"Time to sell the {car_type}!")
                del cars[car_type]

    elif 'Refuel' in command:
        command1, car_type, fuel = command.split(' : ')
        fuel = int(fuel)
        if car_type in cars.keys():
            # if current_car == cars[current_car]:
            cars[car_type][1] += int(fuel)
            if cars[car_type][1] > 75:

                deff = cars[car_type][1] - 75
                fuel -= deff
                cars[car_type][1] = 75

                print(f"{car_type} refueled with {fuel} liters")
            else:
                print(f"{car_type} refueled with {fuel} liters")



    elif 'Revert' in command:
        command1, car_type, kilometers = command.split(' : ')
        if car_type in cars.keys():
            # if current_car == cars[current_car]:
            cars[car_type][0] -=  int(kilometers)
            if cars[car_type][0] < 10000:
                cars[car_type][0] = 10000
            else:
                print(f"{car_type} mileage decreased by {kilometers} kilometers")

for car in cars.keys():

    print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")