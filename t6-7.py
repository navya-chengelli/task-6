l = [2, 3, 5, 3, 7, 2, 8]
def find_first_non_repeating(l):
    element_count = {}
    for num in l:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
    for num in l:
        if element_count[num] == 1:
            return num
    return None
first_non_repeating = find_first_non_repeating(l)
if first_non_repeating is not None:
    print("First non-repeating element:", first_non_repeating)
else:
    print("No non-repeating element found.")