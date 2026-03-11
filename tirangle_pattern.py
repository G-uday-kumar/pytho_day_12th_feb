if __name__=="__main__":
    row=5

    for i in range(1, row + 1):
        for j in range(1,row+1-i):
            print(" ",end=" ")
        for j in range(row,row-i,-1):
            print(j,end=" ")
        for j in range(row+2-i,row+1):
            print(j,end=" ")
        print()
    for i in range(1,row+1):
        for j in range(1,row+1-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(i-1,0,-1):
            print(j,end=" ")
        print()
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1


just a sampele and its a relation
    for i in range(1,row+1):
        for j in range(1,row+1-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(6-j,end=" ")
        for j in range(i-1,0,-1):
            print(6-j,end=" ")
        print()
        #         5
        #       5 4 5
        #     5 4 3 4 5
        #   5 4 3 2 3 4 5
        # 5 4 3 2 1 2 3 4 5

    for i in range(1, row + 1):
        for j in range(1,row+1-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print("*",end=" ")
        for j in range(1,i):
            print("*",end=" ")
        print()
    for i in range(row-1,0,-1):
        for j in range(1,row+1-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print("*",end=" ")
        for j in range(1,i):
            print("*",end=" ")
        print()
    #         *
    #       * * *
    #     * * * * *
    #   * * * * * * *
    # * * * * * * * * *
    #   * * * * * * *
    #     * * * * *
    #       * * *
    #         *

    for i in range(1, row + 1):
        for j in range(1,row+1-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(i-1,0,-1):
            print(j,end=" ")
        print()
    for i in range(row-1,0,-1):
        for j in range(1,row+1-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(i-1,0,-1):
            print(j,end=" ")
        print()
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
#   1 2 3 4 3 2 1
#     1 2 3 2 1
#       1 2 1
#         1

    #
    for i in range(1, row + 1):
        for j in range(1,row+1-i):
            print(" ",end=" ")
        for j in range(row,row-i,-1):
            print(j,end=" ")
        for j in range(row+2-i,row+1):
            print(j,end=" ")
        print()
    for i in range(row-1, 0,-1):
        for j in range(1,row+1-i):
            print(" ",end=" ")
        for j in range(row,row-i,-1):
            print(j,end=" ")
        for j in range(row+2-i,row+1):
            print(j,end=" ")
        print()
    #     #         5
        #       5 4 5
        #     5 4 3 4 5
        #   5 4 3 2 3 4 5
        # 5 4 3 2 1 2 3 4 5
        #   5 4 3 2 3 4 5
        #     5 4 3 4 5
        #       5 4 5
        #         5


        #
        #
        for i in range(1,row+1):
            for j in range(1,row+1-i):
                print(" ",end=" ")
            for j in range(row-i+1,row+1):
                print(j,end=" ")
            for j in range(row-1,row-i,-1):
                print(j,end=" ")
            print()
        for i in range(row-1,0,-1):
            for j in range(1, row + 1 - i):
                print(" ", end=" ")
            for j in range(row - i + 1, row + 1):
                print(j, end=" ")
            for j in range(row - 1, row - i, -1):
                print(j, end=" ")
            print()

        #
        #         5
        #       4 5 4
        #     3 4 5 4 3
        #   2 3 4 5 4 3 2
        # 1 2 3 4 5 4 3 2 1
        #   2 3 4 5 4 3 2
        #     3 4 5 4 3
        #       4 5 4
        #         5


        #
        for i in range(1,row+1):
            for j in range(1,row+1-i):
                print(" ",end=" ")
            for j in range(i,0,-1):
                print(j,end=" ")
            for j in range(2,i+1):
                print(j,end=" ")
            print()
        for i in range(row-1, 0,-1):
            for j in range(1,row+1-i):
                print(" ",end=" ")
            for j in range(i,0,-1):
                print(j,end=" ")
            for j in range(2,i+1):
                print(j,end=" ")
            print()
#
#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5
#   4 3 2 1 2 3 4
#     3 2 1 2 3
#       2 1 2
#         1



