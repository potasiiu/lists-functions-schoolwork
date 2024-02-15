"""This is a program that will keep track of details for a taxi.
It will start with asking for the taxi drivers name and the get details for the trip
at the end it will print out all the details."""
base_cost = 10
costperminute = 2
triptime = []
tripcosts = []


# Gives average values and rounding
def average_value(float_list, decimals):
    list_sum = sum(float_list)
    average = list_sum/len(float_list)
    average_round = round(average, decimals)
    return average_round


# Makes sure the number value inputted is a valid input
def number_check(question):
    error = "\nPlease enter a valid input."
    num = ""
    while not num:
        try:
            num = float(input(question))
            return num
        except ValueError:
            print(error)


# Calculates the cost of each trip depending on the time of the trip
def trip_cost():
    minutes = number_check("How long wast the trip (in minutes): ")
    cost = base_cost + minutes * costperminute
    print(f"The trip cost ${cost}")
    tripcosts.append(cost)
    triptime.append(minutes)


# Ends the day and gives the total time of all trips + total income + average time and average cost of all trips
def conclusion(driver_name):
    total_trip_time = sum(triptime)
    average_trip_time = average_value(triptime, 2)
    total_trip_cost = sum(tripcosts)
    average_trip_cost = average_value(tripcosts, 2)
    print(f"Drivers Name: {driver_name}"
          f"\nTotal time of all trips: {total_trip_time}"
          f"\nAverage time of all trips: {average_trip_time}"
          f"\nTotal income of the day: {total_trip_cost}"
          f"\nAverage cost of all trips: {average_trip_cost}")


# Start function to begin the program
def start():
    drivers_name = input("Enter the drivers name: ")
    while True:
        user_input = input("\nStart a new trip (Y/N): ").lower()
        if user_input == "yes" or user_input == "y":
            trip_cost()
        elif user_input == "no" or user_input == "n":
            conclusion(drivers_name)
            break
        else:
            print("Invalid input. Please try again.")


# Main Routine
start()
