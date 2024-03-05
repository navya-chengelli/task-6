def distribute_mangoes(bags, students):
    if len(bags) < students:
        return -1  
    bags.sort()  
    min_difference = float('inf') 
    for i in range(len(bags) - students + 1):
        min_difference = min(min_difference, bags[i + students - 1] - bags[i])

    return min_difference
bags = [3, 7, 2, 5, 9, 8]
students = 3
min_diff = distribute_mangoes(bags, students)

if min_diff != -1:
    print(f"Minimum difference between bags given to students: {min_diff}")
else:
    print("Not enough bags for each student.")
