# module_ListFunction.py

def find_max(lst):
    """Find the maximum value in a list."""
    return max(lst)

def find_min(lst):
    """Find the minimum value in a list."""
    return min(lst)

def calculate_sum(lst):
    """Calculate the sum of all elements in a list."""
    return sum(lst)

def compute_average(lst):
    """Compute the average of a list."""
    return sum(lst) / len(lst)

def determine_median(lst):
    """Determine the median of a list."""
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2

    if n % 2 == 0:
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        median = sorted_lst[mid]
    
    return median
