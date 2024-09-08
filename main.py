# Function to convert a tuple into a list
def tuple_to_list(tup):
    # Convert tuple to list
    converted_list = list(tup)
    return converted_list

# Sample tuple
sample_tuple = (1, 2, 3, 4, 5)

# Convert the sample tuple to a list
converted_list = tuple_to_list(sample_tuple)

# Print the original tuple and the converted list
print("Original tuple:", sample_tuple)
print("Converted list:", converted_list)
