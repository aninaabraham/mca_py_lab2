# module_DictOperations.py

def merging_Dict(*args):
    """Merge multiple dictionaries into one."""
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

def find_common_keys(*args):
    """Find common keys in multiple dictionaries."""
    if not args:
        return set()
    
    common_keys = set(args[0].keys())
    for d in args[1:]:
        common_keys.intersection_update(d.keys())
    return common_keys

def invert_dict(d):
    """Invert a dictionary, swapping keys and values, grouping keys with the same value."""
    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict

def find_common_key_value_pairs(*args):
    """Find common key-value pairs across multiple dictionaries."""
    if not args:
        return set()
    
    common_pairs = set(args[0].items())
    for d in args[1:]:
        common_pairs.intersection_update(d.items())
    return common_pairs
