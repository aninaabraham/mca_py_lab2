import module_dictionary_operations as do

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
dict3 = {'a': 1, 'b': 2, 'e': 6}

# Demonstrate merging_Dict
merged = do.merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)

# Demonstrate find_common_keys
common_keys = do.find_common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys)

# Demonstrate invert_dict
inverted = do.invert_dict(dict1)
print("Inverted Dictionary of dict1:", inverted)

# Demonstrate find_common_key_value_pairs
common_pairs = do.find_common_key_value_pairs(dict1, dict2, dict3)
print("Common Key-Value Pairs:", common_pairs)
