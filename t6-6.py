list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
def find_duplicates(list1, list2, list3):
    combined_list = list1 + list2 + list3
    element_count = {}
    for element in combined_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    duplicates = []
    for element, count in element_count.items():
        if count > 1:
            duplicates.append(element)
    
    return duplicates
duplicates = find_duplicates(list1, list2, list3)
print("Duplicates:", duplicates)
