# list_ops.py - performs the requested list operations

my_list = []                        # Create an empty list
my_list.append(10)                  # Append 10
my_list.append(20)                  # Append 20
my_list.append(30)                  # Append 30
my_list.append(40)                  # Append 40

my_list.insert(1, 15)               # Insert 15 at the second position (index 1)
my_list.extend([50, 60, 70])        # Extend with [50, 60, 70]
my_list.pop()                       # Remove the last element

my_list.sort()                      # Sort in ascending order

print("Final list:", my_list)       # Show the final list
try:
    print("Index of 30:", my_list.index(30))  # Print index of value 30
except ValueError:
    print("30 is not in the list")
