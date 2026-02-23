#  Find Largest in List
def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


# Count Even Numbers
def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count


#  Sum of List
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total


#  Reverse List (without using reverse())
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


#  Search Element
def search(lst, target):
    for num in lst:
        if num == target:
            return True
    return False



# Main Testing

print("Largest:", find_largest([2,3,5,8,9,4]))
print("Count Even:", count_even([1,2,3,4,6]))
print("Sum List:", sum_list([1,2,3,4]))
print("Reverse:", reverse_list([1,2,3,4]))
print("Search 8:", search([1,5,8,9], 8))