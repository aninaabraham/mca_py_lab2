# module_SetOperations.py

def add_element(s, element):
    """Add an element to a set, ensuring no errors if the element is already present."""
    s.add(element)
    return s

def remove_element(s, element):
    """Remove an element from a set, ensuring no errors if the element is not present."""
    s.discard(element)
    return s

def union_intersection(s1, s2):
    """Return the union and intersection of two sets, handling empty sets correctly."""
    union_set = s1 | s2
    intersection_set = s1 & s2
    return union_set, intersection_set

def difference(s1, s2):
    """Return the difference S1−S2, handling empty sets correctly."""
    return s1 - s2

def is_subset(s1, s2):
    """Check if set S1 is a subset of set S2, handling empty sets correctly."""
    return s1 <= s2

def set_length(s):
    """Find the length of a set without using the len() function."""
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    """Compute the symmetric difference of two sets."""
    return s1 ^ s2

def power_set(s):
    s=list((s))
    power_set=[[]]
    for ele in s:
        new_subsets=[subset+[ele]for subset in power_set]
        power_set.extend(new_subsets)
    return power_set
def unique_subsets(s):
    """Get all unique subsets of a given set."""
    subsets = power_set(s)
    unique_subsets = set(frozenset(subset) for subset in subsets)
    return unique_subsets
