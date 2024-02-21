"""This is a program that stores the cars available for a group of staff to borrow for a day, and it keeps track of
which cars have been booked out. The program will ask the user how many seats they will need and will show which
cars are available."""
car_types = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsibishi Airtrek",
             "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ace"] # List that holds the car types
car_seats = [2, 4, 4, 4, 4, 4, 7, 12, 12] # Lists the amount of seats each car will have
car_numbers = list(range(1, 10)) # Gives each car a number value
booked_car_types = [] # Empty list for the car types that have been booked
booked_car_seats = [] # Empty list for the number of seats of each car that has been booked
booked_car_numbers = [] # Empty list for booked cars of each number value
booker_names = [] # Stores the names of the bookers
exitValue = -1 # Used to exit the program


# Ensures valid integer.
def int_check(input_prompt):
    error_message = "Please enter a valid integer. Try again."
    while True:
        try:
            number = int(input(input_prompt))
            return number
        except ValueError:
            print(error_message)


# Shows the amount of available cars for the amount of seats needed
def print_available_cars(seats_needed):
    print("")
    for i, car in enumerate(car_types):
        print(f"{i + 1}. {car}, {car_seats[i]} seats {"".join(["(not enough seats)"] if car_seats[i] < seats_needed else [])}")


# Asks the user which car they want to book
def book_cars():
    while True:
        booked_car_menu_index = int_check(f"Please input the number for the car you "
                                         f"want to book: (Exit Value: {exitValue}) ")
        if 1 <= booked_car_menu_index <= len(car_types):
            break
        elif booked_car_menu_index == exitValue or (not car_types):
            return True
        else:
            print(f"Invalid input. Please input a integer between 1 and {len(car_types)}.")
    name = input("Input your name: ").title()
    booker_names.append(name)
    print(f"A {car_types[booked_car_menu_index - 1]} has been successfully booked by {name}.")
    booked_car_types.append(car_types[booked_car_menu_index - 1])
    booked_car_seats.append(car_seats[booked_car_menu_index - 1])
    booked_car_numbers.append(car_numbers[booked_car_menu_index - 1])
    car_types.pop(booked_car_menu_index - 1)
    car_seats.pop(booked_car_menu_index - 1)
    car_numbers.pop(booked_car_menu_index - 1)


# Gives the statistics including if all cars are booked and who booked which cars
def print_stats():
    if booked_car_types:
        print("\nAll booked cars:")
        for i, car in enumerate(booked_car_types):
            print(f"{booked_car_numbers[i]}. {car} (booked by {booker_names[i]})")
    else:
        print("No cars were booked.")


# Function to start the code
def start():
    end_program = False
    while not end_program:
        seats_needed = int_check("\nHow many seats do you need in the vehicle? ")
        if seats_needed == exitValue:
            break
        print_available_cars(seats_needed)
        end_program = book_cars()
    print_stats()


# Main Function
start()
