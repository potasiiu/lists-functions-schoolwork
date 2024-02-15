def add_child_name(child_list):
    # Ask for the name of the child
    child_name = input("Enter the name of the child: ")

    # Add the child's name to the list
    child_list.append(child_name)

    # Print a confirmation message
    print(f"{child_name} has been added to the list.")


# Example usage:
children_list = []  # Initialize an empty list to store child names

# Add names to the list using the function
add_child_name(children_list)
add_child_name(children_list)

# Print the final list of child names
print("List of child names:", children_list)