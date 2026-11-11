# Program to remove duplicate elements from a list
original_list = [10, 20, 30, 20, 40, 10, 50, 30]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original List with Duplicates:", original_list)
print("Cleaned List (Unique only):  ", unique_list)
