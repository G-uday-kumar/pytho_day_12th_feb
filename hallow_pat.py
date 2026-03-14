if __name__ == '__main__':
    # row=5
    # for i in range(1,row+1):
    #     for j in range(1,row+1):
    #         if i==1 or j==1 or i==row or j==row:
    #             print("*",end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()
    #
    # * * * * *
    # *       *
    # *       *
    # *       *
    # * * * * *


    # diagolans inside hallo
    # row = 5
    # for i in range(1, row + 1):
    #     for j in range(1, row + 1):
    #         if i == 1 or j == 1 or i == row or j == row or i==j or row+1-i==j:
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()
# * * * * *
# * *   * *
# *   *   *
# * *   * *
# * * * * *

    # row = 10
    # for i in range(1, row + 1):
    #     for j in range(1, row + 1):
    #         if  i == j or row + 1 - i == j or i==5 or j==5 or j==5 or i==6 or j==6:
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()
# * * * * * * * * * *
# * *             * *
# *   *         *   *
# *     *     *     *
# *       * *       *
# *       * *       *
# *     *     *     *
# *   *         *   *
# * *             * *
# * * * * * * * * * *

    # row = 10
    # for i in range(1, row + 1):
    #     for j in range(1, row + 1):
    #         if  i == j or row + 1 - i == j or i==5 or j==5 or j==5 or i==6 or j==6:
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()
# *       * *       *
#   *     * *     *
#     *   * *   *
#       * * * *
# * * * * * * * * * *
# * * * * * * * * * *
#       * * * *
#     *   * *   *
#   *     * *     *
# *       * *       *

    # row=9
    # for i in range(1, row + 1):
    #     for j in range(1, row + 1):
    #         if i==1 or j==1 or i==row or i==j or row+1-i==j or j==row or (row+1)//2==i or (row+1)//2==j:
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()
# * * * * * * * * *
# * *     *     * *
# *   *   *   *   *
# *     * * *     *
# * * * * * * * * *
# *     * * *     *
# *   *   *   *   *
# * *     *     * *
# * * * * * * * * *

    # row=9
    # for i in range(1,row+1):
    #     for j in range(1,row+1):
    #         if i==1 or j==1 or i==row or j==row or i==j or row+1-i==j or (row+1)//2==i or (row+1)//2==j:
    #             print(j,end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()
        # 1 2 3 4 5 6 7 8 9
        # 1 2     5     8 9
        # 1   3   5   7   9
        # 1     4 5 6     9
        # 1 2 3 4 5 6 7 8 9
        # 1     4 5 6     9
        # 1   3   5   7   9
        # 1 2     5     8 9
        # 1 2 3 4 5 6 7 8 9

    # row=5
    # for i in range(1,1+row):
    #     for j in range(1,1+row):
    #         if i==j or i==1 or j==row:
    #             print(j,end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()

        # 1 2 3 4 5
        #   2     5
        #     3   5
        #       4 5
        #         5

    # row=5
    # for i in range(1,row+1):
    #     for j in range(1,row+1):
    #         if i==j or j==1 or i==row:
    #             print(i,end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()
# 1
# 2 2
# 3   3
# 4     4
# 5 5 5 5 5


# now for a heart
#     for i in range(0,6):
#         for j in range(0,7):
#             if (i==1 and j%3==0)or(i==0 and j%3!=0) or i-2==j or i+j==8:
#                 print("*",end=" ")
#             elif(i==2 and j==2):
#                 print("R",end=" ")
#             elif (i == 2 and j == 3):
#                 print("C", end=" ")
#             elif (i == 2 and j == 4):
#                 print("B", end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
    #   * *   * *
    # *     *     *
    # *   R C B   *
    #   *       *
    #     *   *
    #       *


    # for i in range(0,6):
    #     for j in range(0,7):
    #         if (i==1 and j%3==0)or(i==0 and j%3!=0) or i-2==j or i+j==8:
    #             print("*",end=" ")
    #         elif(i==2 and j==2):
    #             print("R",end=" ")
    #         elif (i == 2 and j == 3):
    #             print("C", end=" ")
    #         elif (i == 2 and j == 4):
    #             print("B", end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()
    #
    # for i in range(4,-1,-1):
    #     for j in range(0,7):
    #         if (i==1 and j%3==0)or(i==0 and j%3!=0) or i-2==j or i+j==8:
    #             print("*",end=" ")
    #         elif(i==2 and j==2):
    #             print("R",end=" ")
    #         elif (i == 2 and j == 3):
    #             print("C", end=" ")
    #         elif (i == 2 and j == 4):
    #             print("B", end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()
#   * *   * *
# *     *     *
# *   R C B   *
#   *       *
#     *   *
#       *
#     *   *
#   *       *
# *   R C B   *
# *     *     *
#   * *   * *



    for i in range(0,):
        for i in range(0,6):
            for j in range(0,7):
                if (i==1 and j%3==0)or(i==0 and j%3!=0) or i-2==j or i+j==8:
                    print("*",end=" ")
                elif(i==2 and j==2):
                    print("R",end=" ")
                elif (i == 2 and j == 3):
                    print("C", end=" ")
                elif (i == 2 and j == 4):
                    print("B", end=" ")
                else:
                    print(" ",end=" ")
            print()


