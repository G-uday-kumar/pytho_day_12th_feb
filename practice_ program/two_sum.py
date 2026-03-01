def two_sum(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return True
    return False


print(two_sum([2,7,11,15], 9))