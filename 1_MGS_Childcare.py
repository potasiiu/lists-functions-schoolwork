"""This is a program that adds the names of children to a list and then keeps them
in a roll"""


def dropoff(child_list):
    # Asks for the name of the child
    child_name = input("Enter the name of your child: ")

    # Add the child's name to a list
    child_list.append(child_name)

    # Print a confirmation message
    print(f"Thank you for dropping off {child_name} at MGS Childcare.")


def pickup(child_list):
    if not child_list:
        print("List is empty. No child to remove.")
        return

    # Asks for the name of the child
    child_name = input("Enter the name of the child to remove: ")

    try:
        # Removes the child from the list
        child_list.remove(child_name)
        print(f"Thank you for picking up {child_name}.")
    except ValueError:
        print(f"{child_name} was not detected on our roll. No changes have been made.")


def calcCost():
    hours = int(input("Enter the amount of hours of childcare required: "))
    cost = hours * 12
    print(f"The cost for dropping your child off for {hours}hrs is ${cost}.")


def list_children():
    if not children_list:
        print("There are currently no children in the child care. ")
    else:
        for i, child in enumerate(children_list):
            print(f"{i + 1}. {child}")
        if len(children_list) == 1:
            print(f"There is currently 1 child in the child care.")
        else:
            print(f"There are currently {len(children_list)} children in the child care.")



# Main Routine
children_list = []  # Empty list to hold the children's name
choice = 0
while choice != 5:
    print("-----------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("Please pick one of the options below.")
    print("-----------------------------------------------------------------")
    print()
    print("Press 1 to dropoff a child")
    print("Press 2 to pickup a child")
    print("Press 3 to calculate hourly cost")
    print("Press 4 to print the roll")
    print("Press 5 to exit the system")
    print()
    choice = int(input("Enter your choice (a number between 1 - 5): "))
    print()

    if choice == 1:
        dropoff(children_list)

    elif choice == 2:
        pickup(children_list)

    elif choice == 3:
        calcCost()

    elif choice == 4:
        list_children()

    else:
        print("Farewell, thank you for using MGS Childcare.")
