# This is project to learn LIST in Python
C1_teams = ["TOT", "ARS", "CHE", "MUN"] # In Python, list is created using square brackets []
print(C1_teams)  # Output the entire list
#List can list any data type, in 1 [] we can have multiple data types
mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)  # Output the mixed data type list  

# Accessing elements in a list using indexing
first_team = C1_teams[0]  # Access the first element
print("First team:", first_team)
last_team = C1_teams[-1]  # Access the last element
print("Last team:", last_team)

# Modifying elements in a list
C1_teams[1] = "LIV"  # Change the second element
print("Modified list:", C1_teams)

# Adding elements to a list using append() and insert()
C1_teams.append("LEI")  # Add to the end of the list
print("After append:", C1_teams)
C1_teams.insert(2, "EVE")  # Insert at index 2
print("After insert:", C1_teams)

# Removing elements from a list using remove() and pop()
C1_teams.remove("CHE")  # Remove by value
print("After remove:", C1_teams)
removed_team = C1_teams.pop(3)  # Remove by index
print("After pop:", C1_teams)
print("Removed team:", removed_team)

# List slicing
subset_teams = C1_teams[1:3]  # Get a slice from index 1 to 2
print("Subset of teams:", subset_teams)

# List length using len()
list_length = len(C1_teams)
print("Number of teams in the list:", list_length)

# Looping through a list
print("Teams in the list:")
for team in C1_teams:
    print(team)
# Checking membership using 'in' keyword
is_arsenal_in_list = "ARS" in C1_teams
print("Is Arsenal in the list?", is_arsenal_in_list)# Sorting a list
C1_teams.sort()  # Sort the list in ascending order
print("Sorted list:", C1_teams)      