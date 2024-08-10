# l1=[1,7,90,948,76]
# l1.sort()
# print(l1);
# l1.reverse()
# print(l1);
# l1.insert(4,904);
# print(l1);
# print(l1.pop(3));
# print(l1);
# Sample list
# Sample list
sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# List functions and methods
print(f"Original list: {sample_list}")

length = len(sample_list) 
print(f"Length of the list: {length}")

sample_list.append(8)       
print(f"List after append(8): {sample_list}")

sample_list.insert(2, 7)    
print(f"List after insert(2, 7): {sample_list}")

sample_list.remove(1)       
print(f"List after remove(1): {sample_list}")

popped_item = sample_list.pop(3)             
print(f"Item popped from index 3: {popped_item}")
print(f"List after pop(3): {sample_list}")

index_of_item = sample_list.index(5)      
print(f"Index of first occurrence of 5: {index_of_item}")

count_of_item = sample_list.count(5)      
print(f"Count of 5 in the list: {count_of_item}")

sample_list.sort()            
print(f"List after sort(): {sample_list}")

sample_list.reverse()      
print(f"List after reverse(): {sample_list}")

copy_list = sample_list.copy()            
print(f"Copy of the list: {copy_list}")

sample_list.clear()          
print(f"List after clear(): {sample_list}")

