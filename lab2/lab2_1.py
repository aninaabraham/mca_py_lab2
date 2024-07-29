# main_ListOperations.py

import module_ListFunction as lf

# Creating lists using Python comprehensions
list1 = [x for x in range(1, 11)]  # List of numbers from 1 to 10
list2 = [x**2 for x in range(1, 11)]  # List of squares of numbers from 1 to 10
list3 = [x for x in range(10, 0, -1)]  # List of numbers from 10 to 1 in reverse
list4 = [x for x in range(2, 21, 2)]  # List of even numbers from 2 to 20
list5 = [x for x in range(1, 20, 2)]  # List of odd numbers from 1 to 19

# Demonstrating the use of module functions
print("List 1:", list1)
print("Max:", lf.find_max(list1))
print("Min:", lf.find_min(list1))
print("Sum:", lf.calculate_sum(list1))
print("Average:", lf.compute_average(list1))
print("Median:", lf.determine_median(list1))

print("\nList 2:", list2)
print("Max:", lf.find_max(list2))
print("Min:", lf.find_min(list2))
print("Sum:", lf.calculate_sum(list2))
print("Average:", lf.compute_average(list2))
print("Median:", lf.determine_median(list2))

print("\nList 3:", list3)
print("Max:", lf.find_max(list3))
print("Min:", lf.find_min(list3))
print("Sum:", lf.calculate_sum(list3))
print("Average:", lf.compute_average(list3))
print("Median:", lf.determine_median(list3))

print("\nList 4:", list4)
print("Max:", lf.find_max(list4))
print("Min:", lf.find_min(list4))
print("Sum:", lf.calculate_sum(list4))
print("Average:", lf.compute_average(list4))
print("Median:", lf.determine_median(list4))

print("\nList 5:", list5)
print("Max:", lf.find_max(list5))
print("Min:", lf.find_min(list5))
print("Sum:", lf.calculate_sum(list5))
print("Average:", lf.compute_average(list5))
print("Median:", lf.determine_median(list5))
