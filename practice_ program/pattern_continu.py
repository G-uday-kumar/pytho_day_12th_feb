if __name__ == '__main__':
#     print("in the form of a reverse num order")
#     row=int(input("enter the row number:-"))
#     for i in range(1,row+1):
#         for  j in range(row,0,-1):
#             print(j,end=" ")
#         print()
#
#     print("in the form of a reverse num order")
#     # row = int(input("enter the row number:-"))
#     for i in range(1, row + 1):
#         for j in range(1,i+1):
#                 print(j, end=" ")
#         print()
# #o/p
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5
#     for i in range(1, row + 1):
#         for j in range(1, i + 1):
#             print("*", end=" ")
#         print()
# #*
# # * *
# # * * *
# # * * * *
# # * * * * *
#     for i in range(1,row+1):
#         for j in range(row,row-i,-1):
#             print(j, end=" ")
#         print()
# # 5
# # 5 4
# # 5 4 3
# # 5 4 3 2
# # 5 4 3 2 1
#     row=5
#     for i in range(1,row+1):
#         for j in range(1,i+1):
#             print(j, end=" ")
#         print()
    row=5
    for i in range(1,row+1):
        for j in range(i,i-i,-1):
            print(j,end=" ")
        print()
