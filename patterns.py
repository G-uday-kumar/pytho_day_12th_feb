if __name__=="__main__":
#     print("*")
#     print("*")
#     print("*")
#     print("*")
#
#     print("now check for the using the loop")
#     for i in range(5):
#         print("*")
#     print("now i want all in one line")
#     for i in range(5):
#         print("*",end=" ")
#     print()
#     print("now repeat this lines for multiple times")
#     for i in range(5):
#         print("*",end=" ")
#     print()
#     for i in range(5):
#         print("*",end=" ")
#     print()
#     for i in range(5):
#         print("*",end=" ")
#     print()
#     for i in range(5):
#         print("*",end=" ")
#     print()
#     for i in range(5):
#         print("*",end=" ")
#     print()
#     print("now for rows and column ")
#     for i  in range(5):
#         for j in range(5):
#             print("*",end=" ")
#         print()
#     print("for printing i and j")
#     rows=int(input("enter the number of rows:-"))
#     for i in range(rows):
#         for j in range(rows):
#             print(i,end=" ")
#         print()
#     rows = int(input("enter the number of rows:-"))
#     for i in range(rows):
#         for j in range(rows):
#             print(i, end=" ")
#         print()
#
    print("write for the triangle")
    row=int(input("enter the number of rows:-"))
    for i in range(5):
        for j in range(5):
            if i!=j:
                print(" ",end="")
                continue
            print("*",end="")
        print()
