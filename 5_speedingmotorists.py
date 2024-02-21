"""A Program that checks for how much over the limit an individual was speeding and charging them the right
amount. It also checks for certain individuals with an arrest warrant."""


# Ensures valid input.
def int_test(input_prompt):
    error_message = "Please enter a valid integer. Try again."
    while True:
        try:
            number = int(input(input_prompt))
            return number
        except ValueError:
            print(error_message)


# Makes sure the name inputted is or isn't a person with a warrant and tells if they are or not
def get_name(name):
    wanted = ["James Wilson", "Helga Norman", "Zachary Conroy"]

    for wanted_name in wanted:
        if wanted_name == name:
            print(f"{name} - Warrant to Arrest")
            return


# Gives the costs for hte speeds above limit
def calc_fine(speed_above_limit):
    if speed_above_limit < 10:
        return 30
    elif speed_above_limit <= 14:
        return 80
    elif speed_above_limit <= 19:
        return 120
    elif speed_above_limit <= 24:
        return 170
    elif speed_above_limit <= 29:
        return 230
    elif speed_above_limit <= 34:
        return 300
    elif speed_above_limit <= 39:
        return 400
    elif speed_above_limit <= 44:
        return 510
    else:
        return 630


# Asks for teh persons name and asks for their speed above limit and gives a fine
def give_fine(fine_number):
    name = input(f"Please input the name of the #{fine_number} person speeding: ").title()
    get_name(name)
    speed = int_test("Please input the kph above speed limit: ")
    fine = calc_fine(speed)
    print(f"{name} will be fined ${fine} for speeding {speed}kph above the speed limit")
    return fine


# Asks for the number of fines and gives the total
def start():
    number_of_fines = int_test("Input the number of fines: ")
    total_fine = 0
    i = 1
    while i <= number_of_fines:
        total_fine += give_fine(i)
        i += 1
    print(f"Total amount of fines: ${total_fine}")


# Main Routine
start()


