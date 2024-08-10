# Creating sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 1. Adding an element to a set
set1.add(7)

# 2. Removing an element from a set (raises KeyError if the element is not found)
set1.remove(7)

# 3. Removing an element from a set without raising an error if the element is not found
set1.discard(8)

# 4. Checking if an element is in a set
has_three = 3 in set1

# 5. Union of two sets
union_set = set1.union(set2)

# 6. Intersection of two sets
intersection_set = set1.intersection(set2)

# 7. Difference of two sets
difference_set = set1.difference(set2)

# 8. Symmetric difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2)

# 9. Checking if a set is a subset of another set
is_subset = set1.issubset(set2)

# 10. Checking if a set is a superset of another set
is_superset = set1.issuperset(set2)

# 11. Clearing all elements in a set
# set1.clear()

print('Set after add and remove:', set1)
print('Contains 3:', has_three)
print('Union:', union_set)
print('Intersection:', intersection_set)
print('Difference:', difference_set)
print('Symmetric Difference:', symmetric_difference_set)
print('Is subset:', is_subset)
print('Is superset:', is_superset)
print('Set after clear:', set1)
