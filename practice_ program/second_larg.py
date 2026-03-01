def second_largest(lst):
    largest = lst[0]
    second = None

    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second


print(second_largest([5, 2, 9, 1, 7]))