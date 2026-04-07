def anti_clock(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[len(arr) - 1] = temp
    # return arr
    print(arr)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    # waste of time
    # for i in range(4003):
    #     anti_clock(arr)
    #
    # print(arr)

    # for time compplexity
    for i in range(4003%len(arr)):
        anti_clock(arr)
    print(arr)


