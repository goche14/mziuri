list1 = [1, 2, 3, 4, 5, 2]
list2 = [4, 5, 6, 7, 2, 2]
common_elements = []

for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)

count_common = len(common_elements)

print(common_elements)
print(count_common)