# main_SetOperations.py

import module_SetOperations as so

# Create some sets for demonstration
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set()  # Empty set

# Demonstrate add_element
print("Add element to set1:", so.add_element(set1, 6))

# Demonstrate remove_element
print("Remove element from set1:", so.remove_element(set1, 6))
print("Remove non-existing element from set1:", so.remove_element(set1, 10))

# Demonstrate union_intersection
union, intersection = so.union_intersection(set1, set2)
print("Union of set1 and set2:", union)
print("Intersection of set1 and set2:", intersection)

# Demonstrate difference
print("Difference set1 - set2:", so.difference(set1, set2))

# Demonstrate is_subset
print("Is set1 a subset of set2:", so.is_subset(set1, set2))
print("Is set3 a subset of set1:", so.is_subset(set3, set1))

# Demonstrate set_length
print("Length of set1:", so.set_length(set1))

# Demonstrate symmetric_difference
print("Symmetric difference of set1 and set2:", so.symmetric_difference(set1, set2))

# Demonstrate power_set
print("Power set of set1:", so.power_set(set1))

# Demonstrate unique_subsets
print("Unique subsets of set1:", so.unique_subsets(set1))
