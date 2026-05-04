import copy
ol=[[1,2,3],[4,5,6],[7,8,"a"]]
# print(ol)
# nl=ol
# print(nl)
# nl[2][2]=9
# print(nl)
# print(ol)

# [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print("cloning shallow copy")
# nl=copy.copy(ol)
# print(ol)
# print(nl)
# nl[2][2]=9
# print(nl)
# print(ol)

# [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# print("cloning Deep copy")
# nl=copy.deepcopy(ol)
# print(ol)
# print(nl)
# nl[2][2]=9
# print(nl)
# print(ol)
#
# # [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# # [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]


outer_list=[1,2,3,4,5,6,7,8]
# print(outer_list)
# niw=copy.copy(outer_list)
# print(niw)
# niw[3]="uday"
# print(niw)
# print(outer_list)


print(outer_list)
print(id(outer_list))
# print(id(niw))
niw=copy.copy(outer_list)
print(niw)
niw[3]="uday"
print(niw)
print(outer_list)
print(id(outer_list))
print(id(niw))

# print(outer_list)
# print(id(outer_list))
# # print(id(niw))
# niw=copy.deepcopy(outer_list)
# print(niw)
# niw[3]="uday"
# print(niw)
# print(outer_list)
# print(id(outer_list))
# print(id(niw))