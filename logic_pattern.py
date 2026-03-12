if __name__ == '__main__':
    # using one extra variable method
    # row=5
    # for i in range(1,row+1):
    #     for j in range(1,i+1):
    #         print("*",end=" ")
    #     print()
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    # row=5
    # for i in range(1,row+1):
    #     k=1
    #     for j in range(1,i+1):
    #         print(k,end=" ")
    #         k+=1
    #     print()
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5

    # row=5
    # for i in range(1,row+1):
    #     k=row
    #     for j in range(1,i+1):
    #         print(k,end=" ")
    #         k-=1
    #     print()
    # # 5
    # 5 4
    # 5 4 3
    # 5 4 3 2
    # 5 4 3 2 1

    # row=5
    # for i in range(1,row+1):
    #     k=row-i+1
    #     for j in range(1,i+1):
    #         print(k,end=" ")
    #         k+=1
    #     print()
    #
        # 5
        # 4 5
        # 3 4 5
        # 2 3 4 5
        # 1 2 3 4 5

#     row=5
#     for i in range(1,row+1):
#         k=i
#         for j in range(1,i+1):
#             print(k,end=" ")
#             k-=1
#         print()
# # 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

#     row=5
#     for i in range(1,row+1):
#         k=i
#         for j in range(1,i+1):
#             print(k,end=" ")
#             k+=1
#         print()

# 1
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9

    # row=5
    # for i in range(1,row+1):
    #     k=row
    #     for j in range(1,i+1):
    #         print(k,end=" ")
    #         k+=1
    #     print()
    # 5
    # 5 6
    # 5 6 7
    # 5 6 7 8
    # 5 6 7 8 9

    # row=5
    # k=1
    # for i in range(1,row+1):
    #     for j in range(1,i+1):
    #         print(k,end=" ")
    #         k+=1
    #     print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

    # row=5
    # k=1+97
    # for i in range(1,row+1):
    #     for j in range(1,i+1):
    #         print(chr(k),end=" ")
    #         k+=1
    #     print()
# b
# c d
# e f g
# h i j k
# l m n o p

    # row=5
    # k=1+64
    # for i in range(1,row+1):
    #     for j in range(1,i+1):
    #         print(chr(k),end=" ")
    #         k+=1
    #     print()
# A
# B C
# D E F
# G H I J
# K L M N O


    # row=5
    # k=1
    # for i in range(1,row+1):
    #     for j in range(1,i+1):
    #         if k%2==0:
    #             print(0,end=" ")
    #         else:
    #             print(1,end=" ")
    #         k+=1
    #     print()

    # row = 5
    # k = 1
    # for i in range(1, row + 1):
    #     for j in range(1, i + 1):
    #         print(k%2,end=" ")
    #         k+=1
    #     print()
# 1
# 0 1
# 0 1 0
# 1 0 1 0
# 1 0 1 0 1

    # row=5
    # k = 0
    # for i in range(1, row + 1):
    #     for j in range(1, i + 1):
    #         if k==5:
    #             k=0
    #         print(k,end=" ")
    #             # print(k,end=" ")
    #         k+=1
    #     print()

# 0
# 1 2
# 3 4 0
# 1 2 3 4
# 0 1 2 3 4
    row=5
    k=1
    for i in range(1, row + 1):
        for j in range(1, i + 1):
            print(k%5,end=" ")
            k+=1
        print()

