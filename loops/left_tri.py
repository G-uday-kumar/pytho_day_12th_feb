rows = 6
for i in range(1, rows + 1):
    # print spaces
    for s in range(rows - i):
        print(" ", end=" ")
    # print stars
    for j in range(i):
        print("*", end=" ")
    print()
