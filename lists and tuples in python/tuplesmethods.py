# Sample tuple
sample_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

# Tuple methods and functions
length = len(sample_tuple)                 # Get the length of the tuple
index_of_item = sample_tuple.index(5)      # Get the index of the first occurrence of an item
count_of_item = sample_tuple.count(5)      # Count the occurrences of an item
min_value = min(sample_tuple)              # Get the minimum value in the tuple
max_value = max(sample_tuple)              # Get the maximum value in the tuple
sum_value = sum(sample_tuple)              # Get the sum of all values in the tuple

# Output the results
print(f"Original tuple: {sample_tuple}")
print(f"Length of the tuple: {length}")
print(f"Index of first occurrence of 5: {index_of_item}")
print(f"Count of 5 in the tuple: {count_of_item}")
print(f"Minimum value in the tuple: {min_value}")
print(f"Maximum value in the tuple: {max_value}")
print(f"Sum of all values in the tuple: {sum_value}")

# Sample tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)

# Concatenation of tuples
concatenated_tuple = tuple1 + tuple2 + tuple3

# Output the results
print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Tuple 3: {tuple3}")
print(f"Concatenated tuple: {concatenated_tuple}")

# Sample tuple
sample_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slicing tuples
slice1 = sample_tuple[2:5]      # Elements from index 2 to 4 (inclusive)
slice2 = sample_tuple[:5]       # Elements from the start to index 4 (inclusive)
slice3 = sample_tuple[5:]       # Elements from index 5 to the end
slice4 = sample_tuple[::2]      # Every second element from the start to the end
slice5 = sample_tuple[::-1]     # All elements in reverse order

# Output the results
print(f"Original tuple: {sample_tuple}")
print(f"Slice 1 (2:5): {slice1}")
print(f"Slice 2 (:5): {slice2}")
print(f"Slice 3 (5:): {slice3}")
print(f"Slice 4 (every 2nd element): {slice4}")
print(f"Slice 5 (reverse order): {slice5}")

# Sample tuple
sample_tuple = (1, 2, 3)

# Unpacking tuples
a, b, c = sample_tuple

# Output the results
print(f"Original tuple: {sample_tuple}")
print(f"Unpacked values: a={a}, b={b}, c={c}")

# Unpacking with * operator
sample_tuple = (1, 2, 3, 4, 5)
a, *b, c = sample_tuple

# Output the results
print(f"Original tuple: {sample_tuple}")
print(f"Unpacked values with *: a={a}, b={b}, c={c}")
